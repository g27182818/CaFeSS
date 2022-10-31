# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:36:32 2022

@author: PROFESSIONAL
"""

import PySimpleGUI as sg
import os
from PIL import Image
import PIL
import glob
import datetime

sg.set_options(font=("Helvetica", 5), text_justification='center')
# Set short name for Helvetica
hv = 'Helvetica'
os.getcwd()
w, h = sg.Window.get_screen_size()

fixed_height = 200
image = Image.open(os.path.abspath(
    os.path.join('resources', 'Proyect_Logo.png')))
height_percent = (fixed_height / float(image.size[1]))
width_size = int((float(image.size[0]) * float(height_percent)))
image = image.resize((width_size, fixed_height))
image.save('resources/Logos_documentación1.png')


fixed_height1 = 450
image1 = Image.open(os.path.abspath(
    os.path.join('resources', 'probe.png')))
height_percent1 = (fixed_height1 / float(image1.size[1]))
width_size1 = int((float(image1.size[0]) * float(height_percent1)))
image1 = image1.resize((width_size1, fixed_height1))
image1.save('resources/probe1.png')


sg.theme('LightBrown11')
e = datetime.datetime.now()

col1 = [[sg.Text(' ' * 25,  size=(
    25, 1), font=(hv, 9)), sg.Text('Fermentación del Cacao',  size=(
        22, 1), font=(hv, 30)), sg.Text('2.0',  size=(
            3, 1), font=(hv, 9)), sg.Text(' ' * 15,  size=(
                15, 1), font=(hv, 9)), sg.Button('About us', key='about',
                                                 size=(9, 1), font=(
                                                     hv, 8)), sg.Exit()], [sg.Text('═' * 125, font=(hv, 8))],
    [sg.Text(' ' * 10, size=(
        10, 1), font=(hv, 9)), sg.Text('En lectura', key='lectura',  size=(10, 1), font=(hv, 10)), sg.Text('', size=(10, 1)), sg.Button('Iniciar', button_color='white on green', key='inicio', size=(10, 1), font=(
            hv, 9)),  sg.Text('Día #', key='dia', size=(20, 1), font=(hv, 25)), sg.Button('Finalizar', button_color='white on red', key='fin', size=(10, 1), font=(hv, 9))], [sg.Text('═' * 125, font=(hv, 8))],
    [sg.Text("Fecha de inicio:   %s/%s/%s" % (e.day, e.month, e.year),  size=(25, 1), font=(hv, 10)), sg.Text(' ' * 3, size=(
        3, 1)),
     sg.Text('Fecha final estimada:',  size=(16, 1), font=(hv, 10)), sg.Text('Elija una ->',
                                                                             key='-FINAL-', size=(12, 1), font=(hv, 10)),
     sg.CalendarButton("Fecha final", close_when_date_chosen=True, format='%d/%m/%Y',
                       target='-FINAL-',  font=(hv, 10), no_titlebar=False), sg.Text(' ' * 14, size=(
                           14, 1)),
     sg.Text('Número de Fermentadores detectados: ',  size=(32, 1), font=(hv, 10)), sg.Text('1',  key='nfer', size=(2, 1), font=(hv, 10))],
    [sg.Text('═' * 125, font=(hv, 8))],

    [sg.Text('Nombre encargado:',  size=(16, 1), font=(hv, 10)), sg.Input(
        default_text='Ingrese su nombre', key='encargado', size=(26, 1), font=(hv, 10)), sg.Text(' ' * 1,  size=(
            1, 1)), sg.Text('Ubicación:',  size=(10, 1), font=(hv, 10)), sg.Input(
        default_text='Ingrese su ubicación', key='ubicacion', size=(26, 1), font=(hv, 10)), sg.Text(' ' * 8,  size=(
            8, 1)), sg.Text('Tamaño',  size=(6, 1), font=(hv, 10)),  sg.InputCombo(('Grande', 'Pequeño'), size=(10, 2), font=(hv, 10), key='tamaño', default_value='Grande')]]

col2 = [[sg.Text('Panel de opciones gráficas', font=(hv, 15))],
        [sg.Text('Tipo de Gráfica:', font=(hv, 12))],
        [sg.InputCombo(('Gráficas completas', 'Violin plot', 'Sensores por fermentador',
                        'Promedio y desviación estándar', 'Perfil 3D', 'Cámara termica'), size=(40, 10), font=(hv, 13), key='graphtype', default_value='Gráficas completas')],
        [sg.Text('Fermentador a graficar:', font=(hv, 12))],
        [sg.InputCombo(('Fermentador 1', 'Fermentador 2', 'Fermentador 3', 'Fermentador 4'), size=(40, 10), font=(hv, 13), key='combofer', default_value='Fermentador 1'),

         sg.Button('Graficar', key='buttongraficar',
                   size=(13, 1), font=(hv, 13))],
        [sg.Checkbox('Incluir datos ambientales', key='checkamb',
                     size=(50, 1), default=True, font=(hv, 11))],
        [sg.Checkbox('Resampling', key='checkresamp',
                     size=(50, 1), default=True, font=(hv, 11))],
        [sg.Text('Fecha inicial gráfica:',  size=(22, 1), font=(hv, 10)), sg.Text('Elija una ->',
                                                                                  key='-INICIALG-', size=(12, 1), font=(hv, 10)),
        sg.CalendarButton("Fecha inicial", close_when_date_chosen=True, format='%d/%m/%Y',
                          target='-INICIALG-',  font=(hv, 10), no_titlebar=False), sg.Text(' ' * 14, size=(
                              14, 1))],
        [sg.Text('Fecha final gráfica:',  size=(20, 1), font=(hv, 10)), sg.Text('Elija una ->',
                                                                                key='-FINALG-', size=(12, 1), font=(hv, 10)),
         sg.CalendarButton("Fecha final", close_when_date_chosen=True, format='%d/%m/%Y',
                           target='-FINALG-',  font=(hv, 10), no_titlebar=False), sg.Text(' ' * 14, size=(
                               14, 1))],
        [sg.Button('Mostrar desempeño semanal',
                   key='buttondesempeño', size=(30, 1), font=(hv, 13))],
        [sg.Text('═' * 80, font=(hv, 8))]]
col3 = [[sg.Text('Registro de eventos', font=(hv, 15)), sg.Text('', font=(hv, 11), size=(30, 1)), sg.Button('Guardar Evento', button_color='white on black',
                                                                                                            key='buttonnota', size=(20, 1), font=(hv, 10))],
        [sg.Multiline(default_text='Escribir apuntes del proceso',
                      key='multiline', size=(80, 4), font=("Helvetica", 11))],
        [sg.Button('Registrar Volteo',
                   key='volteo', size=(63, 1), font=(hv, 13))],
        [sg.Text('Ubicación de datos', font=(hv, 15))],
        [sg.Input(default_text='rutaglobal', key='fileinput', size=(60, 1), font=(
            hv, 11)), sg.Text('', size=(2, 1)), sg.Button('Cambiar Ubicación', key='buttonfile', size=(15, 1), font=(hv, 11))],
        [sg.Text('═' * 80, font=(hv, 8))],
        [sg.Text(' ' * 80, font=(hv, 8))],
        [sg.Text(' ' * 80, font=(hv, 8))],
        [sg.Text(' ' * 80, font=(hv, 8))],

        [sg.Text(' ' * 80, font=(hv, 8))]

        ]

colprin = [
    [sg.Image(os.path.abspath(os.path.join('resources', 'Logos_documentación1.png')), size=(
        width_size, fixed_height)), sg.Column(col1)],
    #  [sg.Text('═' * 210, font=(hv, 8))],
    # [sg.Text('', key='lectura',  size=(40, 1), font=(hv, 10)), sg.Text('', size=(5, 1)), sg.Button('Iniciar', button_color='white on green', key='inicio', size=(10, 1), font=(
    #   hv, 9)),  sg.Text('Día #', key='dia', size=(20, 1), font=(hv, 25)), sg.Button('Finalizar', button_color='white on red', key='fin', size=(10, 1), font=(hv, 9))],
    [sg.Text('═' * 173, font=(hv, 8))],
    [sg.Text('Condiciones Ambientales', size=(36, 1), font=(hv, 23)),
     sg.Text('', size=(5, 1), font=(hv, 10)),
     sg.Text('Fermentadores', size=(34, 1), font=(hv, 23))],
    [sg.Text(' ' * 5,  size=(
        5, 1), font=(hv, 9)), sg.Text('  --  °C ',  key='Tamb', size=(6, 1), font=(hv, 40)),
     sg.Text(' ', size=(8, 1), font=(hv, 20)),
     sg.Text('  --  %', size=(6, 1), font=(hv, 40), key='Hamb'),
     sg.Text(' ', size=(9, 1), font=(hv, 40)),
     sg.Text(' --  °C', size=(6, 1), font=(hv, 40), key='Tfer')],
    [sg.Text('Temperatura', size=(28, 1), font=(hv, 14)),
        sg.Text('Humedad', size=(28, 1), font=(hv, 14)),
        sg.Text('', size=(17, 1), font=(hv, 8)),
        sg.Text('Temperatura Promedio', size=(38, 1), font=(hv, 14))],
    [sg.Text('═' * 173, font=(hv, 8))],
    [sg.Column(col2), sg.Column(col3)],

    [sg.Image(os.path.abspath(os.path.join('resources', 'probe1.png')), size=(
        width_size1, fixed_height1))]

]


layout = [[sg.Column(colprin, scrollable=True,
                     vertical_scroll_only=True, size_subsample_height=1)]]


window = sg.Window('Control Ambiental Fermentación', layout,
                   location=(0, 0), size=(w, h), resizable=True, finalize=True)
# window.Maximize()


while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
window.close()
