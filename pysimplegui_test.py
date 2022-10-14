import PySimpleGUI as sg
import os

sg.set_options(font=("Helvetica", 5), text_justification='center')
# Set short name for Helvetica
hv = 'Helvetica'

w,h=sg.Window.get_screen_size()
    
layout = [
    [ sg.Text('', size=(300, 1)),sg.Button('X', key='cerrar',size=(2, 1))],
    [sg.Image(os.path.join('resources','Biomicrosystems_logo.png'), size=(2,1)), sg.Text('Mapeo Fermentación',  size=(25, 1), font=(hv, 30))],
    [sg.Text('═' * 210, font=(hv, 8))],  
    [sg.Text('',key='lectura',  size=(40, 1), font=(hv, 10)), sg.Text('', size=(5, 1)),sg.Button('Iniciar', button_color='white on green',key='inicio',size=(10, 1),font=(hv, 9)),  sg.Text('Día #', key='dia',size=(20, 1), font=(hv, 25)),sg.Button('Finalizar', button_color='white on red', key='fin',size=(10, 1),font=(hv, 9))],
     [sg.Text('═' * 210, font=(hv, 8))],
    [sg.Text('Condiciones Ambientales', size=(34, 1), font=(hv, 23)),
     sg.Text('', size=(6,1), font=(hv, 10)),
     sg.Text('Fermentador', size=(34, 1), font=(hv, 23))],
    [sg.Text('  --  °C ',  key = 'Tamb',size=(6, 1), font=(hv, 60)),
     sg.Text(' ', size=(2, 1), font=(hv, 20)),
     sg.Text('  --  %', size=(6, 1), font=(hv, 60), key='Hamb'),
      sg.Text(' ', size=(4, 1), font=(hv, 40)),
     sg.Text(' --  °C', size=(6, 1), font=(hv, 90),key='Tfer')],
       [sg.Text('Temperatura', size=(28, 1), font=(hv, 14)),
        sg.Text('Humedad', size=(28, 1), font=(hv, 14)),
     sg.Text('', size=(22, 1), font=(hv, 10)),
     sg.Text('Temperatura Promedio', size=(38, 1), font=(hv, 14))],
        [sg.Text('═' * 210, font=(hv, 8))],


   [sg.Text('Gráficas',font=(hv, 15)),sg.Text('', size=(85, 1))],
        [sg.Checkbox('Incluir datos ambientales', key = 'checkamb',size=(50,1), default=True, font=(hv, 10))],
    [sg.InputCombo(('Fermentador 1',),size=(40, 10),font=(hv, 13),key='combofer'),
     
    sg.Button('Graficar', key='buttongraficar',size=(13, 1),font=(hv, 13)),
    
    sg.Text('', size=(20, 1),font=(hv, 10)),
    
        
        sg.Text('', size=(2, 1)),sg.Button('Mostrar desempeño semanal', key='buttondesempeño',size=(30, 1),font=(hv, 13))],
           [sg.Text('═' * 210, font=(hv, 8))],
        [sg.Text('Registro de eventos',font=(hv, 15)),sg.Text('',font=(hv, 11), size=(27, 1)),sg.Button('Guardar Evento',button_color='white on black', key='buttonnota',size=(20, 1),font=(hv, 10)),sg.Text('',font=(hv, 10), size=(12, 1)),sg.Text('Ubicación de datos',font=(hv, 15))],

    [sg.Multiline(default_text='Escribir apuntes del proceso', key='multiline',size=(71, 4),font=("Helvetica", 11)),
     sg.Text('', size=(8, 1),font=(hv, 15)),sg.Input(default_text='rutaglobal',key='fileinput',size=(40, 1),font=(hv, 11)),sg.Text('', size=(3, 1)),sg.Button('Cambiar Ubicación', key='buttonfile',size=(15, 1),font=(hv, 11))],
             [sg.Text('═' * 210, font=(hv, 8))]]


window = sg.Window('Control Ambiental Fermentación', layout, location=(0,0), size=(w,h), resizable=True,finalize=True)



while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()