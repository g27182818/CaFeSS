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
from report_gen import make_report
import datetime


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

# This function reads arduino lines and updates the global dataframe of variables, saves updated files, and computes important statistics
def lecturadatos(global_df, line, global_route, datei):
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
    if not os.path.isdir(global_route):
        os.makedirs(global_route)
    
    save_path = os.path.join(global_route, datei.strftime("%Y-%m-%d %H-%M-%S"))    

    # Save both dataframes in excel file. This file is updated with every measurement
    # with pd.ExcelWriter(save_path, engine='xlsxwriter') as writer:
    #     global_df.to_excel(writer, sheet_name='Total_Datos_Fermentacion')
    #     writer.sheets['Total_Datos_Fermentacion'].set_row(2, None, None, {'hidden': True})
    #     per_fermenter_df.to_excel(writer, sheet_name='Promedios_Generales')
    #     per_day_df.to_excel(writer, sheet_name='Promedio_Diario')
    #     writer.sheets['Promedio_Diario'].set_row(2, None, None, {'hidden': True})

    # If this is the first datum then save with headers
    if global_df.shape[0] == 1:
        global_df.to_csv(os.path.join(save_path, 'global_df.csv'))
        per_fermenter_df.to_csv(os.path.join(save_path, 'per_fermenter_df.csv'))
        per_day_df.to_csv(os.path.join(save_path, 'per_day_df.csv'))
    # For the next data just append to the csvs
    elif global_df.shape > 1:
        global_df.iloc[[-1], :].to_csv(os.path.join(save_path, 'global_df.csv'), mode='a', header=None)
        per_fermenter_df.iloc[[-1], :].to_csv(os.path.join(save_path, 'per_fermenter_df.csv'), mode='a', header=None)
        per_day_df.iloc[[-1], :].to_csv(os.path.join(save_path, 'per_day_df.csv'), mode='a', header=None)
    else:
        raise ValueError('GLobal data frame has no data.')
        
    # Descomentar porque actualiza la interfaz
    # # Actualizar informacion en la interfaz
    # window.Element('Tamb').Update(tamb)
    # window.Element('Hamb').Update(hamb)
    # window.Element('Tfer').Update(tfer)

    return global_df

# This function filters a global dataframe with a start and end strings
def filter_global_df(global_df, start_str, end_str):
    start_datetime = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
    return global_df[start_datetime:end_datetime]