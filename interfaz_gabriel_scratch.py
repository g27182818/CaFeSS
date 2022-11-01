#!/usr/bin/python3
# -*- coding: utf-8 -*-

from cProfile import label
from turtle import title
import PySimpleGUI as sg
import datetime
import random
import matplotlib.pyplot as plt
import seaborn as sn
from matplotlib import style
import serial, time, numpy as np
import pandas as pd
import os
from plotting_functions import *
from test_functions import *
from utils import *
from report_gen import make_report



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
datei = datetime.datetime.now()

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


test_df = generate_realistic_test_df(fermenters = 8, sensors = 12, general_noise = 2, start_noise = 2)

# plot_fermenter_sensors(2, test_df, '10min')
# plot_fermenter_average(6, test_df, '1D')
# plot_fermenter_violin(6, test_df, day_night=True)
# plot_fermenter_complete(6, test_df, freq='30min', resample= '1D')
# start = time.time()
# plot_3d_profile(8, test_df)
# end = time.time()
# print(f'It takes {round(end-start, 2)}s to save a heatmap from one fermenter')
make_report(test_df, freq = '30min', resample='1D')
# save_all_3d_plots(test_df)
# make_gif(fermenter=1)

# Test global_df filtering
# test_start = (datetime.datetime.today() + datetime.timedelta(days=2)).replace(hour=8, minute=0).strftime("%Y-%m-%d %H:%M:%S")
# test_end = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S") 
# test_filtered_df = filter_global_df(test_df, test_start, test_end)

##############################################################################
####################### End of Test code #####################################
##############################################################################


# Violin plot que pueda cuadrarse por dias, 12 horas y 6 horas
# Desde la interfaz se debe poder escojer el inicio el final y la frecuencia de muestreo
# Boton para camara terminca en tiempo real

########################################################################################################################
#                                             Simple GUI Section                                                       #
########################################################################################################################

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



# Variables auxiliares
# var=False
# arranque = False
# act=False
# aviso =0
# rutan = rutaglobal+"/notas"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".txt"
# outFile=open(rutan, "a")

# Ciclo de interfaz y lectura continuo
# while True:
    # Propiedades de gui para manejar los eventos
    # event, values = window.read(timeout = 10)

    # # Get boton de inicio
    # if event == 'inicio':
    #     outFile=open(rutan, "a") # El archivo nunca se cierra durante la ejecucion
    #     arranque= True
    #     contdia = datetime.now() #- timedelta(days=7)
    
    # # Chequear si se deben incluir los valores de temperatura y humedad
    # if not(values is None):
    #     checkamb =values['checkamb']
    
    # # Actualizar variable auxiliar relacionada con la temperatura ambiente
    # if checkamb:
    #     incluir = True
    # else:
    #     incluir = False
    
    # # verificar para poner en estado de lectura
    # if((var==False and contador>0)and act==False):
    #         window.Element('lectura').Update('')
    #         act=True
    

    # if (((((int(time.time()-instanteInicial))/60)>1.1) or contador==0)and arranque==True):

    #     # Actualiza variables auxiliares
    #     if(contador==0):
    #         window.Element('lectura').Update('Sin datos')
    #     instanteInicial = time.time()
    #     dif = datetime.now()-contdia
    #     dias = dif.days
    #     window.Element('dia').Update('Día # ' +str(dias))

    #     # Manda mensaje al arduino
    #     arduino1.write(str.encode("SIU"))
    #     print("Escribiendo")
    #     contador = contador+1
    #     var = True

    # if ((((time.time()-instanteInicial)/60)>0.9) and var==True):
    #     window.Element('lectura').Update('En lectura')
    # if (((((time.time()-instanteInicial))/60)>0.93) and var==True):
    #     print("Leyendo")
        
    #     lecturadatos()
    #     var= False
    #     act=False
    # if event == 'buttonnota':
    #     nota = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+"  "+values['multiline']
    #     outFile.write(nota)
    #     window.Element('multiline').Update('')
    #     sg.popup_timed('Nota Guardada', 'Su nota fue almacenada en la ubicación elegida!',keep_on_top=True)

        
    # if event == 'buttonfile':
    #    folder=  sg.popup_get_folder('Porfavor ingrese una nueva ubicación')
    #    if folder == 'OK':
    #        rutaglobal = folder
    #        window.Element('fileinput').Update(rutaglobal)
    #        rutan = rutaglobal+"/notas"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".txt"
    #        outFile.close()
    #        outFile=open(rutan, "a")

       
    # if dias >14:
    #     aviso += 1
    
    
    # if (event == 'fin' or aviso==1) or (event in (sg.WIN_CLOSED, 'cerrar')):       
    #     seg= sg.popup_ok_cancel('¿Está seguro de finalizar la lectura de datos?',keep_on_top=True)  # Shows OK and Cancel buttons
    #     if seg == 'OK':
    #         print('fin')
    #         window.Element('dia').Update('Día # ')
    #         window.Element('lectura').Update('')
    #         window.Element('Tamb').Update('  --  °C ')
    #         window.Element('Hamb').Update('  --  %')
    #         window.Element('Tfer').Update(' --  °C')
    #         outFile.close()
    #         arranque= False
    #         contador=0
    #         var=False

    #         if len(hdh1)!=0:
    #             df= pd.DataFrame([key for key in psg.keys()], columns=['Fecha y hora'])
    #             df['H ambiente 1'] = hdh1
    #             df['T ambiente 1'] = tdh1
    #             df['H ambiente 2'] = hdh2
    #             df['T ambiente 2'] = tdh2
    #             df['Temp 11'] = ds11
    #             df['Temp 12'] = ds12
    #             df['Temp 13'] = ds13
    #             df['Temp 14'] = ds14
    #             df['Temp 15'] = ds15
    #             df['Temp 16'] = ds16
    #             df['Temp 17'] = ds17
    #             df['Temp 18'] = ds18
    #             df['Temp 19'] = ds19
    #             df['Temp 110'] = ds110
    #             df['Temp 111'] = ds111
    #             df['Temp 112'] = ds112

    #             ruta1 = rutaglobal+"/datos"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".xlsx"
    #             df2= pd.DataFrame(diitas, columns=['Día de Fermentación'])
             
    #             df2['H ambiente 1'] = hdhd1 
    #             df2['T ambiente 1'] = tdhd1
    #             df2['H ambiente 2'] = hdhd2
    #             df2['T ambiente 2'] = hdhd2
    #             df2['Temp 11'] = dsd11
    #             df2['Temp 12'] = dsd12
    #             df2['Temp 13'] = dsd13
    #             df2['Temp 14'] = dsd14
    #             df2['Temp 15'] = dsd15
    #             df2['Temp 16'] = dsd16
    #             df2['Temp 17'] = dsd17
    #             df2['Temp 18'] = dsd18
    #             df2['Temp 19'] = dsd19
    #             df2['Temp 110'] = dsd110
    #             df2['Temp 111'] = dsd111
    #             df2['Temp 112'] = dsd112
    #             writer = pd.ExcelWriter(ruta1, engine = 'openpyxl')
    #             df.to_excel(writer, sheet_name='Total_Datos_Fermentacion')
    #             df2.to_excel(writer, sheet_name='Rendimiento Semanal')
    #             writer.save()
    #             writer.close()             #ruta1 = "/Users/SANTIAGO/Desktop/SANTIAGO/Uniandes/Maestría/Temperatura/Agua Calentador 2/rutaa.xlsx"
            
    #         # Inicializar todo en ceroz una vez mas para evitar errores
    #         ds11 = np.zeros((0,1))
    #         ds12 = np.zeros((0,1))
    #         ds13 = np.zeros((0,1))
    #         ds14 = np.zeros((0,1))
    #         ds15 = np.zeros((0,1))
    #         ds16 = np.zeros((0,1))
    #         ds17 = np.zeros((0,1))
    #         ds18 = np.zeros((0,1))
    #         ds19 = np.zeros((0,1))
    #         ds110 = np.zeros((0,1))
    #         ds111 = np.zeros((0,1))
    #         ds112 = np.zeros((0,1))
    #         hdh1 = np.zeros((0,1))
    #         tdh1 = np.zeros((0,1))

    #         hdhd1 = np.zeros((14,))
    #         tdhd1 = np.zeros((14,))
    #         hdhd2 = np.zeros((14,))
    #         tdhd2 = np.zeros((14,))
    #         dsd11 = np.zeros((14,))
    #         dsd12 = np.zeros((14,))
    #         dsd13 = np.zeros((14,))
    #         dsd14 = np.zeros((14,))
    #         dsd15 = np.zeros((14,))
    #         dsd16 = np.zeros((14,))
    #         dsd17 = np.zeros((14,))
    #         dsd18 = np.zeros((14,))
    #         dsd19 = np.zeros((14,))
    #         dsd110 = np.zeros((14,))
    #         dsd111 = np.zeros((14,))
    #         dsd112 = np.zeros((14,))
    #         ds21 = np.zeros((0,1))
    #         ds22 = np.zeros((0,1))
    #         ds23 = np.zeros((0,1))
    #         ds24 = np.zeros((0,1))
    #         ds25 = np.zeros((0,1))
    #         ds26 = np.zeros((0,1))
    #         hdh2 = np.zeros((0,1))
    #         tdh2 = np.zeros((0,1))

    #         ds31 = np.zeros((0,1))
    #         ds32 = np.zeros((0,1))
    #         ds33 = np.zeros((0,1))
    #         ds34 = np.zeros((0,1))
    #         ds35 = np.zeros((0,1))
    #         ds36 = np.zeros((0,1))
    #         hdh3 = np.zeros((0,1))
    #         tdh3 = np.zeros((0,1))

    #         ds41 = np.zeros((0,1))
    #         ds42 = np.zeros((0,1))
    #         ds43 = np.zeros((0,1))
    #         ds44 = np.zeros((0,1))
    #         ds45 = np.zeros((0,1))
    #         ds46 = np.zeros((0,1))
    #         hdh4 = np.zeros((0,1))
    #         tdh4 = np.zeros((0,1))

    #         ds51 = np.zeros((0,1))
    #         ds52 = np.zeros((0,1))
    #         ds53 = np.zeros((0,1))
    #         ds54 = np.zeros((0,1))
    #         ds55 = np.zeros((0,1))
    #         ds56 = np.zeros((0,1))
    #         hdh5 = np.zeros((0,1))
    #         tdh5 = np.zeros((0,1))

    #         ds61 = np.zeros((0,1))
    #         ds62 = np.zeros((0,1))
    #         ds63 = np.zeros((0,1))
    #         ds64 = np.zeros((0,1))
    #         ds65 = np.zeros((0,1))
    #         ds66 = np.zeros((0,1))
    #         hdh6 = np.zeros((0,1))
    #         tdh6 = np.zeros((0,1))

    #         ds71 = np.zeros((0,1))
    #         ds72 = np.zeros((0,1))
    #         ds73 = np.zeros((0,1))
    #         ds74 = np.zeros((0,1))
    #         ds75 = np.zeros((0,1))
    #         ds76 = np.zeros((0,1))
    #         hdh7 = np.zeros((0,1))
    #         tdh7 = np.zeros((0,1))

    #         ds81 = np.zeros((0,1))
    #         ds82 = np.zeros((0,1))
    #         ds83 = np.zeros((0,1))
    #         ds84 = np.zeros((0,1))
    #         ds85 = np.zeros((0,1))
    #         ds86 = np.zeros((0,1))
    #         hdh8 = np.zeros((0,1))
    #         tdh8 = np.zeros((0,1))

    #         ds91 = np.zeros((0,1))
    #         ds92 = np.zeros((0,1))
    #         ds93 = np.zeros((0,1))
    #         ds94 = np.zeros((0,1))
    #         ds95 = np.zeros((0,1))
    #         ds96 = np.zeros((0,1))
    #         hdh9 = np.zeros((0,1))
    #         tdh9 = np.zeros((0,1))
    #         if event in (sg.WIN_CLOSED, 'cerrar'):
    #             arduino1.close() #Finalizamos la comunicacion
    #             break    


   
    # if event == 'buttongraficar':
    #     fer = int(values['combofer'].split[-1])
    #     draw_plot(fer)

    # if event == 'buttondesempeño':
    #     draw_rend()

# window.close()