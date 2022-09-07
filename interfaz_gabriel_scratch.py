#!/usr/bin/python3
# -*- coding: utf-8 -*-

from cProfile import label
from turtle import title
import PySimpleGUI as sg
from datetime import datetime, date, time, timedelta
import random
import matplotlib.pyplot as plt
import seaborn as sn
from matplotlib import style
import serial, time, numpy as np
import pandas as pd
import os
from plotting_functions import *

# Matplotlib set axis bellow
plt.rcParams['axes.axisbelow'] = True

# Close previous plt instances
plt.clf()
plt.cla()
plt.close()
sg.ChangeLookAndFeel('DarkBrown6')
dias=0

# Define global variables
global rutaglobal

# Define initial values of global variables
rutaglobal= 'datos'
# rutaglobal=  "/home/pi/Raspduino"
datei = datetime.now()

# Define initial value of auxiliary variables
contdia = 0
instanteInicial = time.time()
contador =0
incluir=True

# Print start message
print("Starting!")


# ------ Menu Definition ------ #
menudef = [['Menu', ['Info', 'Propiedades','Salir']]]


# Serial communication setup
serial_path = '/dev/ttyUSB0'
serial_speed = 9600
# Test code uncomment the next line to get real function
arduino1 = serial.Serial()
# arduino1 = serial.Serial(serial_path)


# This function recieves an arduino line and retuns a pandas dataframe 
def get_pd_from_line(line):
    
    # Split line by fermenter
    splited_line = line.split('f')[1:] # splited line for fermenter
    # Number of fermenters
    num_fer = len(splited_line)

    # List of ambient temperature and humidity
    amb_list = line.split('f')[0].split(',')[:-1]

    # Define global dict to store current temperatures
    global_dict = { 't_amb-1': float(amb_list[1]),
                    't_amb-2': float(amb_list[2]),
                    'h_amb-1': float(amb_list[4]),
                    'h_amb-2': float(amb_list[5])}

    # Cycle in each fermenter to compute important things
    for i in range(num_fer):
        # Split each fermenter by comas and dont use the initial number. The if is to handle the last comma
        fermenter_list = splited_line[i].split(',')[1:-1] if i != num_fer-1 else splited_line[i].split(',')[1:]
        fermenter_list = [float(temp) for temp in fermenter_list]
        # Restart fermenter dict just in case
        fermenter_dict = {}
        # Declare fermenter dict
        fermenter_dict = {f'f{i+1}-{j+1}': [fermenter_list[j]] for j in range(len(fermenter_list))}
        # Append current information to global_dict
        global_dict = global_dict | fermenter_dict

    # Get pandas dataframe for current measurement
    output_df = pd.DataFrame.from_dict(global_dict)
    # Put date and time as index
    output_df.index = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    output_df.index = pd.to_datetime(output_df.index)

    # Put multiindex in data
    output_df.columns = pd.MultiIndex.from_tuples([(c.split('-')[0], c.split('-')[1]) for c in output_df.columns])
    
    # Set names 
    output_df.columns.names = [None, 'datetime']

    # Return output dataframe
    return output_df

# This function reads arduino lines and updated the global dataframe of variables, saves updated files, and computes important statistics
def lecturadatos(global_df, line):
    # Uncoment when using arduino
    # arduino_line = arduino1.readline()
    # decoded_arduino_line = arduino_line.decode(encoding = 'utf-8')
    # current_df = get_pd_from_line(decoded_arduino_line)

    # Test code, comment in real application
    current_df = get_pd_from_line(line)
    
    # Concat normal dataframe with current meassures. If global_df has nothing declare it as current_df
    global_df = current_df if global_df.shape[0] == 0 else pd.concat([global_df, current_df])

    # Get per day averages
    per_day_df = global_df.resample('D').mean()
    per_day_df.columns.names = [None, 'datetime']
    # Promedio de todos los sensores por fermentador
    per_fermenter_df = global_df.groupby(level=0, axis=1).mean()
    per_fermenter_df.index.name = 'datetime'

    # Ruta destino para guardar datos en csv
    if not os.path.isdir(rutaglobal):
        os.makedirs(rutaglobal)
    
    save_path = os.path.join(rutaglobal, datei.strftime("%Y-%m-%d %H-%M-%S")+".xlsx")    

    # Save both dataframes in excel file. This file is updated with every measurement
    with pd.ExcelWriter(save_path, engine='xlsxwriter') as writer:
        global_df.to_excel(writer, sheet_name='Total_Datos_Fermentacion')
        writer.sheets['Total_Datos_Fermentacion'].set_row(2, None, None, {'hidden': True})
        per_fermenter_df.to_excel(writer, sheet_name='Promedios_Generales')
        per_day_df.to_excel(writer, sheet_name='Promedio_Diario')
        writer.sheets['Promedio_Diario'].set_row(2, None, None, {'hidden': True})

    # Descomentar porque actualiza la interfaz
    # # Actualizar informacion en la interfaz
    # window.Element('Tamb').Update(tamb)
    # window.Element('Hamb').Update(hamb)
    # window.Element('Tfer').Update(tfer)

    return global_df


# Code to generate a test line
def generate_test_line(num_fer):
    test_str = ''
    # Simulate test ambient temperature and humidity
    t_amb = np.round(10*np.random.rand(2)+20, 2)
    h_amb = np.round(20*np.random.rand(2)+60, 2)
    test_str = test_str + f't_amb,{t_amb[0]},{t_amb[1]},h_amb,{h_amb[0]},{h_amb[1]},'
    # Simulate fermenters sensors
    for i in range(num_fer):
        temp_list = np.round(10*np.random.rand(12)+20, 2)
        test_str = test_str + f'f{i+1}' if i == 0 else test_str + f',f{i+1}'
        for i in range(len(temp_list)):
            test_str = test_str + ',' + str(temp_list[i])   
    return test_str

##############################################################################
####################### Test code ############################################
##############################################################################

# # Number of fermenters
# fermenters = 8
# # Global dataframe to save all data
# global_df = pd.DataFrame()

# plot_fermenter(2, global_df)

# # Test cycle on 100 measures
# for i in range(10):
#     test_measure = generate_test_line(fermenters)
#     global_df = lecturadatos(global_df, test_measure)
#     time.sleep(1)


# Make test for 14 days
# Test parameters
test_fermenters = 8
test_sensors = 12
test_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
test_end = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S")
noise = 1
start_noise = 2

# Make multiindex columns and date rows for 14 days
fermenter_list = [f'f{i+1}' for i in range(test_fermenters)]
sensor_list = [f'{i+1}' for i in range(test_sensors)]
fermenter_columns = pd.MultiIndex.from_product([fermenter_list, sensor_list])
amb_columns = pd.MultiIndex.from_product([['t_amb', 'h_amb'], ['1', '2']])
test_columns = amb_columns.append(fermenter_columns) 
test_index = pd.date_range(start=test_start, end = test_end, freq='10min')


# Generate test data
test_time = np.linspace(0, 5, len(test_index))
test_fermenter_temps = (20 + 30*(1-np.exp(-test_time))).reshape((-1,1))
test_fermenter_matrix = test_fermenter_temps + np.random.randn(1, test_fermenters*test_sensors)*start_noise

test_t_amb_matrix = test_fermenter_temps + np.random.randn(1, 2)*start_noise
test_h_amb_matrix = (50 + 30*(1-np.exp(-test_time))).reshape((-1,1)) + np.random.randn(1, 2)*start_noise

test_matrices = [test_t_amb_matrix, test_h_amb_matrix, test_fermenter_matrix]
test_matrices = [mat + np.random.randn(mat.shape[0], mat.shape[1])*noise for mat in test_matrices] # Add noise
# Join test data
test_data = np.concatenate(tuple(test_matrices), axis=1)

# Declare test_global_df
test_global_df = pd.DataFrame(test_data, index=test_index, columns=test_columns)
# Set names 
test_global_df.columns.names = [None, 'datetime']

plot_fermenter_sensors(2, test_global_df, '10min')
plot_fermenter_average(6, test_global_df, '1D')
plot_fermenter_boxplot(6, test_global_df)
plot_3d_profile(8, test_global_df)

##############################################################################
####################### End of Test code #####################################
##############################################################################



# Hacer que la interfaz arranque
# Violin plot que pueda cuadrarse por dias, 12 horas y 6 horas
# Poner shading de noche en las graficas    
# Frecuencia de muestreo va a ser cada 30 minutos
# Figuras de tamaño fijo
# Desde la interfaz se debe poder escojer el inicio el final y la frecuencia de muestreo
# Boton para camara terminca en tiempo real

# ########################################################################################################################
# #                                             Simple GUI Section                                                       #
# ########################################################################################################################

# w,h=sg.Window.get_screen_size()
    
# layout = [
#     [ sg.Text('', size=(300, 1), justification='center', font=("Helvetica", 5)),sg.Button('X', key='cerrar',size=(2, 1),font=("Helvetica", 5))],
#     [sg.Image('/home/pi/Raspduino/bio1.png'),sg.Text('Mapeo Fermentación',  size=(25, 1), justification='center', font=("Helvetica", 30))],
#     [sg.Text('═' * 210, font=("Helvetica", 8))],  
#     [sg.Text('',key='lectura',  size=(40, 1), justification='center', font=("Helvetica", 10)), sg.Text('', size=(5, 1)),sg.Button('Iniciar', button_color='white on green',key='inicio',size=(10, 1),font=("Helvetica", 9)),  sg.Text('Día #', key='dia',size=(20, 1), justification='center', font=("Helvetica", 25)),sg.Button('Finalizar', button_color='white on red', key='fin',size=(10, 1),font=("Helvetica", 9))],
#     [sg.Text('═' * 210, font=("Helvetica", 8))],
#     [sg.Text('Condiciones Ambientales', size=(34, 1), justification='center', font=("Helvetica", 23)),
#      sg.Text('', size=(6,1), justification='center', font=("Helvetica", 10)),
#      sg.Text('Fermentador', size=(34, 1), justification='center', font=("Helvetica", 23))],
#     [sg.Text('  --  °C ',  key = 'Tamb',size=(6, 1), justification='center', font=("Helvetica", 60)),
#      sg.Text(' ', size=(2, 1), justification='center', font=("Helvetica", 20)),
#      sg.Text('  --  %', size=(6, 1), justification='center', font=("Helvetica", 60), key='Hamb'),
#       sg.Text(' ', size=(4, 1), justification='center', font=("Helvetica", 40)),
#      sg.Text(' --  °C', size=(6, 1), justification='center', font=("Helvetica", 90),key='Tfer')], #, relief=sg.RELIEF_RIDGE
#     [sg.Text('Temperatura', size=(28, 1), justification='center', font=("Helvetica", 14)),
#     sg.Text('Humedad', size=(28, 1), justification='center', font=("Helvetica", 14)),
#      sg.Text('', size=(22, 1), justification='center', font=("Helvetica", 10)),
#      sg.Text('Temperatura Promedio', size=(38, 1), justification='center', font=("Helvetica", 14))],#
#     [sg.Text('═' * 210, font=("Helvetica", 8))],
#     [sg.Text('Gráficas',font=("Helvetica", 15)),sg.Text('', size=(85, 1))],
#     [sg.Checkbox('Incluir datos ambientales', key = 'checkamb',size=(50,1), default=True,font=("Helvetica", 10))],
#     [sg.InputCombo(('Fermentador 1',),size=(40, 10),font=("Helvetica", 13),key='combofer'), 
#     sg.Button('Graficar', key='buttongraficar',size=(13, 1),font=("Helvetica", 13)),
#     sg.Text('', size=(20, 1),font=("Helvetica", 10)),
#     sg.Text('', size=(2, 1)),sg.Button('Mostrar desempeño semanal', key='buttondesempeño',size=(30, 1),font=("Helvetica", 13))],
#     [sg.Text('═' * 210, font=("Helvetica", 8))],
#     [sg.Text('Registro de eventos',font=("Helvetica", 15)),sg.Text('',font=("Helvetica", 11), size=(27, 1)),sg.Button('Guardar Evento',button_color='white on black', key='buttonnota',size=(20, 1),font=("Helvetica", 10)),sg.Text('',font=("Helvetica", 10), size=(12, 1)),sg.Text('Ubicación de datos',font=("Helvetica", 15))],
#     [sg.Multiline(default_text='Escribir apuntes del proceso', key='multiline',size=(71, 4),font=("Helvetica", 11)),
#     sg.Text('', size=(8, 1),font=("Helvetica", 15)),sg.Input(default_text=rutaglobal,key='fileinput',size=(40, 1),font=("Helvetica", 11)),sg.Text('', size=(3, 1)),sg.Button('Cambiar Ubicación', key='buttonfile',size=(15, 1),font=("Helvetica", 11))],
#     [sg.Text('═' * 210, font=("Helvetica", 8))]]



# window = sg.Window('Control Ambiental Fermentación', layout, location=(0,0), size=(w,h), resizable=True,finalize=True)

# # Variables auxiliares
# var=False
# arranque = False
# act=False
# aviso =0
# rutan = rutaglobal+"/notas"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".txt"
# outFile=open(rutan, "a")

# # Ciclo de interfaz y lectura continuo
# while True:
#     # Propiedades de gui para manejar los eventos
#     event, values = window.read(timeout = 10)

#     # Get boton de inicio
#     if event == 'inicio':
#         outFile=open(rutan, "a") # El archivo nunca se cierra durante la ejecucion
#         arranque= True
#         contdia = datetime.now() #- timedelta(days=7)
    
#     # Chequear si se deben incluir los valores de temperatura y humedad
#     if not(values is None):
#         checkamb =values['checkamb']
    
#     # Actualizar variable auxiliar relacionada con la temperatura ambiente
#     if checkamb:
#         incluir = True
#     else:
#         incluir = False
    
#     # verificar para poner en estado de lectura
#     if((var==False and contador>0)and act==False):
#             window.Element('lectura').Update('')
#             act=True
    

#     if (((((int(time.time()-instanteInicial))/60)>1.1) or contador==0)and arranque==True):

#         # Actualiza variables auxiliares
#         if(contador==0):
#             window.Element('lectura').Update('Sin datos')
#         instanteInicial = time.time()
#         dif = datetime.now()-contdia
#         dias = dif.days
#         window.Element('dia').Update('Día # ' +str(dias))

#         # Manda mensaje al arduino
#         arduino1.write(str.encode("SIU"))
#         print("Escribiendo")
#         contador = contador+1
#         var = True

#     if ((((time.time()-instanteInicial)/60)>0.9) and var==True):
#         window.Element('lectura').Update('En lectura')
#     if (((((time.time()-instanteInicial))/60)>0.93) and var==True):
#         print("Leyendo")
        
#         lecturadatos()
#         var= False
#         act=False
#     if event == 'buttonnota':
#         nota = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+"  "+values['multiline']
#         outFile.write(nota)
#         window.Element('multiline').Update('')
#         sg.popup_timed('Nota Guardada', 'Su nota fue almacenada en la ubicación elegida!',keep_on_top=True)

        
#     if event == 'buttonfile':
#        folder=  sg.popup_get_folder('Porfavor ingrese una nueva ubicación')
#        if folder == 'OK':
#            rutaglobal = folder
#            window.Element('fileinput').Update(rutaglobal)
#            rutan = rutaglobal+"/notas"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".txt"
#            outFile.close()
#            outFile=open(rutan, "a")

       
#     if dias >14:
#         aviso += 1
    
    
#     if (event == 'fin' or aviso==1) or (event in (sg.WIN_CLOSED, 'cerrar')):       
#         seg= sg.popup_ok_cancel('¿Está seguro de finalizar la lectura de datos?',keep_on_top=True)  # Shows OK and Cancel buttons
#         if seg == 'OK':
#             print('fin')
#             window.Element('dia').Update('Día # ')
#             window.Element('lectura').Update('')
#             window.Element('Tamb').Update('  --  °C ')
#             window.Element('Hamb').Update('  --  %')
#             window.Element('Tfer').Update(' --  °C')
#             outFile.close()
#             arranque= False
#             contador=0
#             var=False

#             if len(hdh1)!=0:
#                 df= pd.DataFrame([key for key in psg.keys()], columns=['Fecha y hora'])
#                 df['H ambiente 1'] = hdh1
#                 df['T ambiente 1'] = tdh1
#                 df['H ambiente 2'] = hdh2
#                 df['T ambiente 2'] = tdh2
#                 df['Temp 11'] = ds11
#                 df['Temp 12'] = ds12
#                 df['Temp 13'] = ds13
#                 df['Temp 14'] = ds14
#                 df['Temp 15'] = ds15
#                 df['Temp 16'] = ds16
#                 df['Temp 17'] = ds17
#                 df['Temp 18'] = ds18
#                 df['Temp 19'] = ds19
#                 df['Temp 110'] = ds110
#                 df['Temp 111'] = ds111
#                 df['Temp 112'] = ds112

#                 ruta1 = rutaglobal+"/datos"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".xlsx"
#                 df2= pd.DataFrame(diitas, columns=['Día de Fermentación'])
             
#                 df2['H ambiente 1'] = hdhd1 
#                 df2['T ambiente 1'] = tdhd1
#                 df2['H ambiente 2'] = hdhd2
#                 df2['T ambiente 2'] = hdhd2
#                 df2['Temp 11'] = dsd11
#                 df2['Temp 12'] = dsd12
#                 df2['Temp 13'] = dsd13
#                 df2['Temp 14'] = dsd14
#                 df2['Temp 15'] = dsd15
#                 df2['Temp 16'] = dsd16
#                 df2['Temp 17'] = dsd17
#                 df2['Temp 18'] = dsd18
#                 df2['Temp 19'] = dsd19
#                 df2['Temp 110'] = dsd110
#                 df2['Temp 111'] = dsd111
#                 df2['Temp 112'] = dsd112
#                 writer = pd.ExcelWriter(ruta1, engine = 'openpyxl')
#                 df.to_excel(writer, sheet_name='Total_Datos_Fermentacion')
#                 df2.to_excel(writer, sheet_name='Rendimiento Semanal')
#                 writer.save()
#                 writer.close()             #ruta1 = "/Users/SANTIAGO/Desktop/SANTIAGO/Uniandes/Maestría/Temperatura/Agua Calentador 2/rutaa.xlsx"
            
#             # Inicializar todo en ceroz una vez mas para evitar errores
#             ds11 = np.zeros((0,1))
#             ds12 = np.zeros((0,1))
#             ds13 = np.zeros((0,1))
#             ds14 = np.zeros((0,1))
#             ds15 = np.zeros((0,1))
#             ds16 = np.zeros((0,1))
#             ds17 = np.zeros((0,1))
#             ds18 = np.zeros((0,1))
#             ds19 = np.zeros((0,1))
#             ds110 = np.zeros((0,1))
#             ds111 = np.zeros((0,1))
#             ds112 = np.zeros((0,1))
#             hdh1 = np.zeros((0,1))
#             tdh1 = np.zeros((0,1))

#             hdhd1 = np.zeros((14,))
#             tdhd1 = np.zeros((14,))
#             hdhd2 = np.zeros((14,))
#             tdhd2 = np.zeros((14,))
#             dsd11 = np.zeros((14,))
#             dsd12 = np.zeros((14,))
#             dsd13 = np.zeros((14,))
#             dsd14 = np.zeros((14,))
#             dsd15 = np.zeros((14,))
#             dsd16 = np.zeros((14,))
#             dsd17 = np.zeros((14,))
#             dsd18 = np.zeros((14,))
#             dsd19 = np.zeros((14,))
#             dsd110 = np.zeros((14,))
#             dsd111 = np.zeros((14,))
#             dsd112 = np.zeros((14,))
#             ds21 = np.zeros((0,1))
#             ds22 = np.zeros((0,1))
#             ds23 = np.zeros((0,1))
#             ds24 = np.zeros((0,1))
#             ds25 = np.zeros((0,1))
#             ds26 = np.zeros((0,1))
#             hdh2 = np.zeros((0,1))
#             tdh2 = np.zeros((0,1))

#             ds31 = np.zeros((0,1))
#             ds32 = np.zeros((0,1))
#             ds33 = np.zeros((0,1))
#             ds34 = np.zeros((0,1))
#             ds35 = np.zeros((0,1))
#             ds36 = np.zeros((0,1))
#             hdh3 = np.zeros((0,1))
#             tdh3 = np.zeros((0,1))

#             ds41 = np.zeros((0,1))
#             ds42 = np.zeros((0,1))
#             ds43 = np.zeros((0,1))
#             ds44 = np.zeros((0,1))
#             ds45 = np.zeros((0,1))
#             ds46 = np.zeros((0,1))
#             hdh4 = np.zeros((0,1))
#             tdh4 = np.zeros((0,1))

#             ds51 = np.zeros((0,1))
#             ds52 = np.zeros((0,1))
#             ds53 = np.zeros((0,1))
#             ds54 = np.zeros((0,1))
#             ds55 = np.zeros((0,1))
#             ds56 = np.zeros((0,1))
#             hdh5 = np.zeros((0,1))
#             tdh5 = np.zeros((0,1))

#             ds61 = np.zeros((0,1))
#             ds62 = np.zeros((0,1))
#             ds63 = np.zeros((0,1))
#             ds64 = np.zeros((0,1))
#             ds65 = np.zeros((0,1))
#             ds66 = np.zeros((0,1))
#             hdh6 = np.zeros((0,1))
#             tdh6 = np.zeros((0,1))

#             ds71 = np.zeros((0,1))
#             ds72 = np.zeros((0,1))
#             ds73 = np.zeros((0,1))
#             ds74 = np.zeros((0,1))
#             ds75 = np.zeros((0,1))
#             ds76 = np.zeros((0,1))
#             hdh7 = np.zeros((0,1))
#             tdh7 = np.zeros((0,1))

#             ds81 = np.zeros((0,1))
#             ds82 = np.zeros((0,1))
#             ds83 = np.zeros((0,1))
#             ds84 = np.zeros((0,1))
#             ds85 = np.zeros((0,1))
#             ds86 = np.zeros((0,1))
#             hdh8 = np.zeros((0,1))
#             tdh8 = np.zeros((0,1))

#             ds91 = np.zeros((0,1))
#             ds92 = np.zeros((0,1))
#             ds93 = np.zeros((0,1))
#             ds94 = np.zeros((0,1))
#             ds95 = np.zeros((0,1))
#             ds96 = np.zeros((0,1))
#             hdh9 = np.zeros((0,1))
#             tdh9 = np.zeros((0,1))
#             if event in (sg.WIN_CLOSED, 'cerrar'):
#                 arduino1.close() #Finalizamos la comunicacion
#                 break    


   
#     if event == 'buttongraficar':
#         fer = int(values['combofer'].split[-1])
#         draw_plot(fer)

#     if event == 'buttondesempeño':
#         draw_rend()

# window.close()