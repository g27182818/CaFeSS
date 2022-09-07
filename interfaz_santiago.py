#!/usr/bin/python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from datetime import datetime, date, time, timedelta
import random
import matplotlib.pyplot as plt
from matplotlib import style
import serial, time, numpy as np
import pandas as pd

plt.clf()
plt.cla()
plt.close()
sg.ChangeLookAndFeel('DarkBrown6')
dias=0

# ------ Menu Definition ------ #
menudef = [['Menu', ['Info', 'Propiedades','Salir']]]

serial_path = '/dev/ttyUSB0'
serial_speed = 9600

# Test code uncomment the next line to get real function
arduino1 = serial.Serial()

# arduino1 = serial.Serial(serial_path, serial_speed)
# arduino2 = serial.Serial('/dev/ttyUSB0', 9600)
# arduino3 = serial.Serial('/dev/ttyUSB0', 9600)
# arduino4 = serial.Serial('/dev/ttyUSB0', 9600)
# arduino5 = serial.Serial('/dev/ttyUSB0', 9600)
# arduino6 = serial.Serial('/dev/ttyUSB0', 9600)
# arduino7 = serial.Serial('/dev/ttyUSB0', 9600)
# arduino8 = serial.Serial('/dev/ttyUSB0', 9600)
# arduino9 = serial.Serial('/dev/ttyUSB0', 9600)
siu =False
lectura= ''
global diitas
diitas= ['Dia 0','Dia 1','Dia 2','Dia 3','Dia 4','Dia 5','Dia 6','Dia 7','Dia 8','Dia 9','Dia 10','Dia 11','Dia 12','Dia 13']
ds11 = np.zeros((0,1))
ds12 = np.zeros((0,1))
ds13 = np.zeros((0,1))
ds14 = np.zeros((0,1))
ds15 = np.zeros((0,1))
ds16 = np.zeros((0,1))
ds17 = np.zeros((0,1))
ds18 = np.zeros((0,1))
ds19 = np.zeros((0,1))
ds110 = np.zeros((0,1))
ds111 = np.zeros((0,1))
ds112 = np.zeros((0,1))
dsmean1 = np.zeros((0,1))
hdh1 = np.zeros((0,1))
tdh1 = np.zeros((0,1))

ds21 = np.zeros((0,1))
ds22 = np.zeros((0,1))
ds23 = np.zeros((0,1))
ds24 = np.zeros((0,1))
ds25 = np.zeros((0,1))
ds26 = np.zeros((0,1))
hdh2 = np.zeros((0,1))
tdh2 = np.zeros((0,1))

ds31 = np.zeros((0,1))
ds32 = np.zeros((0,1))
ds33 = np.zeros((0,1))
ds34 = np.zeros((0,1))
ds35 = np.zeros((0,1))
ds36 = np.zeros((0,1))
hdh3 = np.zeros((0,1))
tdh3 = np.zeros((0,1))

ds41 = np.zeros((0,1))
ds42 = np.zeros((0,1))
ds43 = np.zeros((0,1))
ds44 = np.zeros((0,1))
ds45 = np.zeros((0,1))
ds46 = np.zeros((0,1))
hdh4 = np.zeros((0,1))
tdh4 = np.zeros((0,1))

ds51 = np.zeros((0,1))
ds52 = np.zeros((0,1))
ds53 = np.zeros((0,1))
ds54 = np.zeros((0,1))
ds55 = np.zeros((0,1))
ds56 = np.zeros((0,1))
hdh5 = np.zeros((0,1))
tdh5 = np.zeros((0,1))

ds61 = np.zeros((0,1))
ds62 = np.zeros((0,1))
ds63 = np.zeros((0,1))
ds64 = np.zeros((0,1))
ds65 = np.zeros((0,1))
ds66 = np.zeros((0,1))
hdh6 = np.zeros((0,1))
tdh6 = np.zeros((0,1))

ds71 = np.zeros((0,1))
ds72 = np.zeros((0,1))
ds73 = np.zeros((0,1))
ds74 = np.zeros((0,1))
ds75 = np.zeros((0,1))
ds76 = np.zeros((0,1))
hdh7 = np.zeros((0,1))
tdh7 = np.zeros((0,1))

ds81 = np.zeros((0,1))
ds82 = np.zeros((0,1))
ds83 = np.zeros((0,1))
ds84 = np.zeros((0,1))
ds85 = np.zeros((0,1))
ds86 = np.zeros((0,1))
hdh8 = np.zeros((0,1))
tdh8 = np.zeros((0,1))

ds91 = np.zeros((0,1))
ds92 = np.zeros((0,1))
ds93 = np.zeros((0,1))
ds94 = np.zeros((0,1))
ds95 = np.zeros((0,1))
ds96 = np.zeros((0,1))
hdh9 = np.zeros((0,1))
tdh9 = np.zeros((0,1))


global psg0,psg1,psg2,psg3,psg4,psg5,psg6,psg7,psg8,psg9,psg10,psg11,psg12,psg13
global hdhd1,tdhd1,hdhd2,tdhd2,dsd11,dsd12,dsd13,dsd14,dsd15,dsd16,dsd17,dsd18,dsd19,dsd110,dsd111,dsd112
hdhd1 = np.zeros((14,))
tdhd1 = np.zeros((14,))
hdhd2 = np.zeros((14,))
tdhd2 = np.zeros((14,))
dsd11 = np.zeros((14,))
dsd12 = np.zeros((14,))
dsd13 = np.zeros((14,))
dsd14 = np.zeros((14,))
dsd15 = np.zeros((14,))
dsd16 = np.zeros((14,))
dsd17 = np.zeros((14,))
dsd18 = np.zeros((14,))
dsd19 = np.zeros((14,))
dsd110 = np.zeros((14,))
dsd111 = np.zeros((14,))
dsd112 = np.zeros((14,))
global datei
datei = datetime.now()
psg0 = np.zeros([16,0])
psg1 = np.zeros([16,0])
psg2 = np.zeros([16,0])
psg3 = np.zeros([16,0])
psg4 = np.zeros([16,0])
psg5 = np.zeros([16,0])
psg6 = np.zeros([16,0])
psg7 = np.zeros([16,0])
psg8 = np.zeros([16,0])
psg9 = np.zeros([16,0])
psg10 = np.zeros([16,0])
psg11 = np.zeros([16,0])
psg12 = np.zeros([16,0])
psg13 = np.zeros([16,0])
contdia = 0
instanteInicial = time.time()
print("Starting!")
contador =0
global checkamb
checkamb=True
global psg
global keys
global valores
psg={}
keys = psg.keys()
incluir=True
global rutaglobal

rutaglobal= "/home/pi/Raspduino"

def lecturadatos():
    rawString1 = arduino1.readline()
    #print("Leyendo")
    #print(rawString)
    rawS1 = rawString1.decode(encoding = 'utf-8')
    separado1 = rawS1.split(",")
    separado1.pop()
    
    datos=separado1

    datotime = datetime.now()
    global psg0,psg1,psg2,psg3,psg4,psg5,psg6,psg7,psg8,psg9,psg10,psg11,psg12,psg13 
    registro = psg.setdefault(datotime,datos)  
    keys = psg.keys()
    valores = list(psg.values())
    diai = list(psg.items())[0][0].day
    datei = list(psg.items())[0][0]
    diaf = list(psg.items())[-1][0].day
    difdia= diaf -diai
    if difdia == 0:
        psg0 = np.insert(psg0,psg0.shape[1],datos,1)
    elif difdia == 1:
        psg1 = np.insert(psg1,psg1.shape[1],datos,1)
    elif difdia == 2:
        psg2 = np.insert(psg2,psg2.shape[1],datos,1)
    elif difdia == 3:
        psg3 = np.insert(psg3,psg3.shape[1],datos,1)
    elif difdia == 4:
        psg4 = np.insert(psg4,psg4.shape[1],datos,1)
    elif difdia == 5:
        psg5 = np.insert(psg5,psg5.shape[1],datos,1)
    elif difdia == 6:
        psg6 = np.insert(psg6,psg6.shape[1],datos,1)
    elif difdia == 7:
        psg7 = np.insert(psg7,psg7.shape[1],datos,1)
    elif difdia == 8:
        psg8 = np.insert(psg8,psg8.shape[1],datos,1)
    elif difdia == 9:
        psg9 = np.insert(psg9,psg9.shape[1],datos,1)
    elif difdia == 10:
        psg10 = np.insert(psg10,psg10.shape[1],datos,1)
    elif difdia == 11:
        psg11 = np.insert(psg11,psg11.shape[1],datos,1)
    elif difdia == 12:
        psg12 = np.insert(psg12,psg12.shape[1],datos,1)
    elif difdia == 13:
        psg13 = np.insert(psg13,psg13.shape[1],datos,1)
        
    
    global ds11
    ds11 = np.zeros((0,1))
    global ds12
    ds12 = np.zeros((0,1))
    global ds13
    ds13 = np.zeros((0,1))
    global ds14
    ds14 = np.zeros((0,1))
    global ds15
    ds15 = np.zeros((0,1))
    global ds16
    ds16 = np.zeros((0,1))
    global ds17
    ds17 = np.zeros((0,1))
    global ds18
    ds18 = np.zeros((0,1))
    global ds19
    ds19 = np.zeros((0,1))
    global ds110
    ds110 = np.zeros((0,1))
    global ds111
    ds111 = np.zeros((0,1))
    global ds112
    ds112 = np.zeros((0,1))
    global dsmean1
    dsmean1 = np.zeros((0,1))
    global hdh1
    hdh1 = np.zeros((0,1))
    global tdh1
    tdh1 = np.zeros((0,1))

    global ds21,ds22,ds23,ds24,ds25,ds26,hdh2,tdh2,ds31,ds32,ds33,ds34,ds35,ds36,hdh3,tdh3,ds41,ds42,ds43,ds44,ds45,ds46,hdh4,tdh4,ds41,ds42,ds43,ds44,ds45,ds46,hdh4,tdh4,ds51,ds52,ds53,ds54,ds55,ds56,hdh5,tdh5,ds61,ds62,ds63,ds64,ds65,ds66,hdh6,tdh6,ds71,ds72,ds73,ds74,ds75,ds76,hdh7,tdh7,ds71,ds72,ds73,ds74,ds75,ds76,hdh7,tdh7,ds81,ds82,ds83,ds84,ds85,ds86,hdh8,tdh8,ds91,ds92,ds93,ds94,ds95,ds96,hdh9,tdh9
    global hdhd1,tdhd1,hdhd2,tdhd2,dsd11,dsd12,dsd13,dsd14,dsd15,dsd16,dsd17,dsd18,dsd19,dsd110,dsd111,dsd112
    dsd11 = [np.mean(psg0[0]),np.mean(psg1[0]),np.mean(psg2[0]),np.mean(psg3[0]),np.mean(psg4[0]),np.mean(psg5[0]),np.mean(psg6[0]),np.mean(psg7[0]),np.mean(psg8[0]),np.mean(psg9[0]),np.mean(psg10[0]),np.mean(psg11[0]),np.mean(psg12[0]),np.mean(psg13[0])]
    dsd12 = [np.mean(psg0[1]),np.mean(psg1[1]),np.mean(psg2[1]),np.mean(psg3[1]),np.mean(psg4[1]),np.mean(psg5[1]),np.mean(psg6[1]),np.mean(psg7[1]),np.mean(psg8[1]),np.mean(psg9[1]),np.mean(psg10[1]),np.mean(psg11[1]),np.mean(psg12[1]),np.mean(psg13[1])]
    dsd13 = [np.mean(psg0[2]),np.mean(psg1[2]),np.mean(psg2[2]),np.mean(psg3[2]),np.mean(psg4[2]),np.mean(psg5[2]),np.mean(psg6[2]),np.mean(psg7[2]),np.mean(psg8[2]),np.mean(psg9[2]),np.mean(psg10[2]),np.mean(psg11[2]),np.mean(psg12[2]),np.mean(psg13[2])]
    dsd14 = [np.mean(psg0[3]),np.mean(psg1[3]),np.mean(psg2[3]),np.mean(psg3[3]),np.mean(psg4[3]),np.mean(psg5[3]),np.mean(psg6[3]),np.mean(psg7[3]),np.mean(psg8[3]),np.mean(psg9[3]),np.mean(psg10[3]),np.mean(psg11[3]),np.mean(psg12[3]),np.mean(psg13[3])]
    dsd15 = [np.mean(psg0[4]),np.mean(psg1[4]),np.mean(psg2[4]),np.mean(psg3[4]),np.mean(psg4[4]),np.mean(psg5[4]),np.mean(psg6[4]),np.mean(psg7[4]),np.mean(psg8[4]),np.mean(psg9[4]),np.mean(psg10[4]),np.mean(psg11[4]),np.mean(psg12[4]),np.mean(psg13[4])]
    dsd16 = [np.mean(psg0[5]),np.mean(psg1[5]),np.mean(psg2[5]),np.mean(psg3[5]),np.mean(psg4[5]),np.mean(psg5[5]),np.mean(psg6[5]),np.mean(psg7[5]),np.mean(psg8[5]),np.mean(psg9[5]),np.mean(psg10[5]),np.mean(psg11[5]),np.mean(psg12[5]),np.mean(psg13[5])]
    dsd17 = [np.mean(psg0[6]),np.mean(psg1[6]),np.mean(psg2[6]),np.mean(psg3[6]),np.mean(psg4[6]),np.mean(psg5[6]),np.mean(psg6[6]),np.mean(psg7[6]),np.mean(psg8[6]),np.mean(psg9[6]),np.mean(psg10[6]),np.mean(psg11[6]),np.mean(psg12[6]),np.mean(psg13[6])]
    dsd18 = [np.mean(psg0[7]),np.mean(psg1[7]),np.mean(psg2[7]),np.mean(psg3[7]),np.mean(psg4[7]),np.mean(psg5[7]),np.mean(psg6[7]),np.mean(psg7[7]),np.mean(psg8[7]),np.mean(psg9[7]),np.mean(psg10[7]),np.mean(psg11[7]),np.mean(psg12[7]),np.mean(psg13[7])]
    dsd19 = [np.mean(psg0[8]),np.mean(psg1[8]),np.mean(psg2[8]),np.mean(psg3[8]),np.mean(psg4[8]),np.mean(psg5[8]),np.mean(psg6[8]),np.mean(psg7[8]),np.mean(psg8[8]),np.mean(psg9[8]),np.mean(psg10[8]),np.mean(psg11[8]),np.mean(psg12[8]),np.mean(psg13[8])]
    dsd110 = [np.mean(psg0[9]),np.mean(psg1[9]),np.mean(psg2[9]),np.mean(psg3[9]),np.mean(psg4[9]),np.mean(psg5[9]),np.mean(psg6[9]),np.mean(psg7[9]),np.mean(psg8[9]),np.mean(psg9[9]),np.mean(psg10[9]),np.mean(psg11[9]),np.mean(psg12[9]),np.mean(psg13[9])]
    dsd111 = [np.mean(psg0[10]),np.mean(psg1[10]),np.mean(psg2[10]),np.mean(psg3[10]),np.mean(psg4[10]),np.mean(psg5[10]),np.mean(psg6[10]),np.mean(psg7[10]),np.mean(psg8[10]),np.mean(psg9[10]),np.mean(psg10[10]),np.mean(psg11[10]),np.mean(psg12[10]),np.mean(psg13[10])]
    dsd112 = [np.mean(psg0[11]),np.mean(psg1[11]),np.mean(psg2[11]),np.mean(psg3[11]),np.mean(psg4[11]),np.mean(psg5[11]),np.mean(psg6[11]),np.mean(psg7[11]),np.mean(psg8[11]),np.mean(psg9[11]),np.mean(psg10[11]),np.mean(psg11[11]),np.mean(psg12[11]),np.mean(psg13[11])]
    hdhd1 = [np.mean(psg0[12]),np.mean(psg1[12]),np.mean(psg2[12]),np.mean(psg3[12]),np.mean(psg4[12]),np.mean(psg5[12]),np.mean(psg6[12]),np.mean(psg7[12]),np.mean(psg8[12]),np.mean(psg9[12]),np.mean(psg10[12]),np.mean(psg11[12]),np.mean(psg12[12]),np.mean(psg13[12])]
    tdhd1 = [np.mean(psg0[13]),np.mean(psg1[13]),np.mean(psg2[13]),np.mean(psg3[13]),np.mean(psg4[13]),np.mean(psg5[13]),np.mean(psg6[13]),np.mean(psg7[13]),np.mean(psg8[13]),np.mean(psg9[13]),np.mean(psg10[13]),np.mean(psg11[13]),np.mean(psg12[13]),np.mean(psg13[13])]
    hdhd2 = [np.mean(psg0[14]),np.mean(psg1[14]),np.mean(psg2[14]),np.mean(psg3[14]),np.mean(psg4[14]),np.mean(psg5[14]),np.mean(psg6[14]),np.mean(psg7[14]),np.mean(psg8[14]),np.mean(psg9[14]),np.mean(psg10[14]),np.mean(psg11[14]),np.mean(psg12[14]),np.mean(psg13[14])]
    tdhd2 = [np.mean(psg0[15]),np.mean(psg1[15]),np.mean(psg2[15]),np.mean(psg3[15]),np.mean(psg4[15]),np.mean(psg5[15]),np.mean(psg6[15]),np.mean(psg7[15]),np.mean(psg8[15]),np.mean(psg9[15]),np.mean(psg10[15]),np.mean(psg11[15]),np.mean(psg12[15]),np.mean(psg13[15])]
    print(dsd11)
    ds21 = np.zeros((0,1))
    ds22 = np.zeros((0,1))
    ds23 = np.zeros((0,1))
    ds24 = np.zeros((0,1))
    ds25 = np.zeros((0,1))
    ds26 = np.zeros((0,1))
    hdh2 = np.zeros((0,1))
    tdh2 = np.zeros((0,1))

    ds31 = np.zeros((0,1))
    ds32 = np.zeros((0,1))
    ds33 = np.zeros((0,1))
    ds34 = np.zeros((0,1))
    ds35 = np.zeros((0,1))
    ds36 = np.zeros((0,1))
    hdh3 = np.zeros((0,1))
    tdh3 = np.zeros((0,1))

    ds41 = np.zeros((0,1))
    ds42 = np.zeros((0,1))
    ds43 = np.zeros((0,1))
    ds44 = np.zeros((0,1))
    ds45 = np.zeros((0,1))
    ds46 = np.zeros((0,1))
    hdh4 = np.zeros((0,1))
    tdh4 = np.zeros((0,1))

    ds51 = np.zeros((0,1))
    ds52 = np.zeros((0,1))
    ds53 = np.zeros((0,1))
    ds54 = np.zeros((0,1))
    ds55 = np.zeros((0,1))
    ds56 = np.zeros((0,1))
    hdh5 = np.zeros((0,1))
    tdh5 = np.zeros((0,1))

    ds61 = np.zeros((0,1))
    ds62 = np.zeros((0,1))
    ds63 = np.zeros((0,1))
    ds64 = np.zeros((0,1))
    ds65 = np.zeros((0,1))
    ds66 = np.zeros((0,1))
    hdh6 = np.zeros((0,1))
    tdh6 = np.zeros((0,1))

    ds71 = np.zeros((0,1))
    ds72 = np.zeros((0,1))
    ds73 = np.zeros((0,1))
    ds74 = np.zeros((0,1))
    ds75 = np.zeros((0,1))
    ds76 = np.zeros((0,1))
    hdh7 = np.zeros((0,1))
    tdh7 = np.zeros((0,1))

    ds81 = np.zeros((0,1))
    ds82 = np.zeros((0,1))
    ds83 = np.zeros((0,1))
    ds84 = np.zeros((0,1))
    ds85 = np.zeros((0,1))
    ds86 = np.zeros((0,1))
    hdh8 = np.zeros((0,1))
    tdh8 = np.zeros((0,1))

    ds91 = np.zeros((0,1))
    ds92 = np.zeros((0,1))
    ds93 = np.zeros((0,1))
    ds94 = np.zeros((0,1))
    ds95 = np.zeros((0,1))
    ds96 = np.zeros((0,1))
    hdh9 = np.zeros((0,1))
    tdh9 = np.zeros((0,1))
    valores = list(psg.values())
    print(valores)
    print(len(valores))
    for i in range (len(valores)):
        ds11 =np.insert(ds11,ds11.shape[0],valores[i][0])
        ds12 =np.insert(ds12,ds12.shape[0],valores[i][1]) 
        ds13 =np.insert(ds13,ds13.shape[0],valores[i][2]) 
        ds14 =np.insert(ds14,ds14.shape[0],valores[i][3])
        ds15 =np.insert(ds15,ds15.shape[0],valores[i][4])
        ds16 =np.insert(ds16,ds16.shape[0],valores[i][5])
        ds17 =np.insert(ds17,ds17.shape[0],valores[i][6])
        ds18 =np.insert(ds18,ds18.shape[0],valores[i][7]) 
        ds19 =np.insert(ds19,ds19.shape[0],valores[i][8]) 
        ds110 =np.insert(ds110,ds110.shape[0],valores[i][9])
        ds111 =np.insert(ds111,ds111.shape[0],valores[i][10])
        ds112 =np.insert(ds112,ds112.shape[0],valores[i][11])
        hdh1 =np.insert(hdh1,hdh1.shape[0],valores[i][12]) 
        tdh1 =np.insert(tdh1,tdh1.shape[0],valores[i][13])
        hdh2 =np.insert(hdh2,hdh2.shape[0],valores[i][14]) 
        tdh2 =np.insert(tdh2,tdh2.shape[0],valores[i][15])
      #  dsmean1 = np.insert(dsmean1,dsmean1.shape[0],np.mean([valores[i][0],valores[i][1],valores[i][2],valores[i][3],valores[i][4],valores[i][5],valores[i][6],valores[i][7],valores[i][8],valores[i][9],valores[i][10],valores[i][11],valores[i][12]]))   

#     print('dsmean1')    
#     print(dsmean1)

    df= pd.DataFrame([key for key in psg.keys()], columns=['Fecha y hora'])
    df['H ambiente 1'] = hdh1
    df['T ambiente 1'] = tdh1
    df['H ambiente 2'] = hdh2
    df['T ambiente 2'] = tdh2
    df['Temp 11'] = ds11
    df['Temp 12'] = ds12
    df['Temp 13'] = ds13
    df['Temp 14'] = ds14
    df['Temp 15'] = ds15
    df['Temp 16'] = ds16
    df['Temp 17'] = ds17
    df['Temp 18'] = ds18
    df['Temp 19'] = ds19
    df['Temp 110'] = ds110
    df['Temp 111'] = ds111
    df['Temp 112'] = ds112
    
   # df['Temp 1mean'] = dsmean1
#         df['Temp 21'] = ds21
#         df['Temp 22'] = ds22
#         df['Temp 23'] = ds23
#         df['Temp 24'] = ds24
#         df['Temp 25'] = ds25
#         df['Temp 26'] = ds26
#         df['Temp 31'] = ds31
#         df['Temp 32'] = ds32
#         df['Temp 33'] = ds33
#         df['Temp 34'] = ds34
#         df['Temp 35'] = ds35
#         df['Temp 36'] = ds36
#         df['Temp 41'] = ds41
#         df['Temp 42'] = ds42
#         df['Temp 43'] = ds43
#         df['Temp 44'] = ds44
#         df['Temp 45'] = ds45
#         df['Temp 46'] = ds46
#         df['Temp 51'] = ds51
#         df['Temp 52'] = ds52
#         df['Temp 53'] = ds53
#         df['Temp 54'] = ds54
#         df['Temp 55'] = ds55
#         df['Temp 56'] = ds56
#         df['Temp 61'] = ds61
#         df['Temp 62'] = ds62
#         df['Temp 63'] = ds63
#         df['Temp 64'] = ds64
#         df['Temp 65'] = ds65
#         df['Temp 66'] = ds66
#         df['Temp 71'] = ds71
#         df['Temp 72'] = ds72
#         df['Temp 73'] = ds73
#         df['Temp 74'] = ds74
#         df['Temp 75'] = ds75
#         df['Temp 76'] = ds76
#         df['Temp 81'] = ds81
#         df['Temp 82'] = ds82
#         df['Temp 83'] = ds83
#         df['Temp 84'] = ds84
#         df['Temp 85'] = ds85
#         df['Temp 86'] = ds86
#         df['Temp 91'] = ds91
#         df['Temp 92'] = ds92
#         df['Temp 93'] = ds93
#         df['Temp 94'] = ds94
#         df['Temp 95'] = ds95
#         df['Temp 96'] = ds96
#

    ruta1 = rutaglobal+"/datos"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".xlsx"
    global diitas
    diitas= ['Dia 0','Dia 1','Dia 2','Dia 3','Dia 4','Dia 5','Dia 6','Dia 7','Dia 8','Dia 9','Dia 10','Dia 11','Dia 12','Dia 13']
    df2= pd.DataFrame(diitas, columns=['Día de Fermentación'])
 
    df2['H ambiente 1'] = hdhd1 
    df2['T ambiente 1'] = tdhd1
    df2['H ambiente 2'] = hdhd2
    df2['T ambiente 2'] = hdhd2
    df2['Temp 11'] = dsd11
    df2['Temp 12'] = dsd12
    df2['Temp 13'] = dsd13
    df2['Temp 14'] = dsd14
    df2['Temp 15'] = dsd15
    df2['Temp 16'] = dsd16
    df2['Temp 17'] = dsd17
    df2['Temp 18'] = dsd18
    df2['Temp 19'] = dsd19
    df2['Temp 110'] = dsd110
    df2['Temp 111'] = dsd111
    df2['Temp 112'] = dsd112
   # df.to_excel(ruta1)

    writer = pd.ExcelWriter(ruta1, engine = 'openpyxl')
    df.to_excel(writer, sheet_name='Total_Datos_Fermentacion')
    df2.to_excel(writer, sheet_name='Rendimiento Semanal')
    writer.save()
    writer.close()
#         ds21 =np.insert(ds21,ds21.shape[0],valores[i][8])
#         ds22 =np.insert(ds22,ds22.shape[0],valores[i][9]) 
#         ds23 =np.insert(ds23,ds23.shape[0],valores[i][10]) 
#         ds24 =np.insert(ds24,ds24.shape[0],valores[i][11])
#         ds25 =np.insert(ds25,ds25.shape[0],valores[i][12])
#         ds26 =np.insert(ds26,ds26.shape[0],valores[i][13])
#         hdh2 =np.insert(hdh2,hdh2.shape[0],valores[i][14]) 
#         tdh2 =np.insert(tdh2,tdh2.shape[0],valores[i][15])
#         
#         ds31 =np.insert(ds31,ds31.shape[0],valores[i][16])
#         ds32 =np.insert(ds32,ds32.shape[0],valores[i][17]) 
#         ds33 =np.insert(ds33,ds33.shape[0],valores[i][18]) 
#         ds34 =np.insert(ds34,ds34.shape[0],valores[i][19])
#         ds35 =np.insert(ds35,ds35.shape[0],valores[i][20])
#         ds36 =np.insert(ds36,ds36.shape[0],valores[i][21])
#         hdh3 =np.insert(hdh3,hdh3.shape[0],valores[i][22]) 
#         tdh3 =np.insert(tdh3,tdh3.shape[0],valores[i][23])
#         
#         ds41 =np.insert(ds41,ds41.shape[0],valores[i][24])
#         ds42 =np.insert(ds42,ds42.shape[0],valores[i][25]) 
#         ds43 =np.insert(ds43,ds43.shape[0],valores[i][26]) 
#         ds44 =np.insert(ds44,ds44.shape[0],valores[i][27])
#         ds45 =np.insert(ds45,ds45.shape[0],valores[i][28])
#         ds46 =np.insert(ds46,ds46.shape[0],valores[i][29])
#         hdh4 =np.insert(hdh4,hdh4.shape[0],valores[i][30]) 
#         tdh4 =np.insert(tdh4,tdh4.shape[0],valores[i][31])
#         
#         ds51 =np.insert(ds51,ds51.shape[0],valores[i][32])
#         ds52 =np.insert(ds52,ds52.shape[0],valores[i][33]) 
#         ds53 =np.insert(ds53,ds53.shape[0],valores[i][34]) 
#         ds54 =np.insert(ds54,ds54.shape[0],valores[i][35])
#         ds55 =np.insert(ds55,ds55.shape[0],valores[i][36])
#         ds56 =np.insert(ds56,ds56.shape[0],valores[i][37])
#         hdh5 =np.insert(hdh5,hdh5.shape[0],valores[i][38]) 
#         tdh5 =np.insert(tdh5,tdh5.shape[0],valores[i][39])
#         
#         ds61 =np.insert(ds61,ds61.shape[0],valores[i][40])
#         ds62 =np.insert(ds62,ds62.shape[0],valores[i][41]) 
#         ds63 =np.insert(ds63,ds63.shape[0],valores[i][42]) 
#         ds64 =np.insert(ds64,ds64.shape[0],valores[i][43])
#         ds65 =np.insert(ds65,ds65.shape[0],valores[i][44])
#         ds66 =np.insert(ds66,ds66.shape[0],valores[i][45])
#         hdh6 =np.insert(hdh6,hdh6.shape[0],valores[i][46]) 
#         tdh6 =np.insert(tdh6,tdh6.shape[0],valores[i][47])
#         
#         ds71 =np.insert(ds1,ds1.shape[0],valores[i][48])
#         ds72 =np.insert(ds2,ds2.shape[0],valores[i][49]) 
#         ds73 =np.insert(ds3,ds3.shape[0],valores[i][50]) 
#         ds74 =np.insert(ds4,ds4.shape[0],valores[i][51])
#         ds75 =np.insert(ds5,ds5.shape[0],valores[i][52])
#         ds76 =np.insert(ds6,ds6.shape[0],valores[i][53])
#         hdh7 =np.insert(hdh,hdh.shape[0],valores[i][54]) 
#         tdh7 =np.insert(tdh,tdh.shape[0],valores[i][55])
#         
#         ds81 =np.insert(ds81,ds81.shape[0],valores[i][56])
#         ds82 =np.insert(ds82,ds82.shape[0],valores[i][57]) 
#         ds83 =np.insert(ds83,ds83.shape[0],valores[i][58]) 
#         ds84 =np.insert(ds84,ds84.shape[0],valores[i][59])
#         ds85 =np.insert(ds85,ds85.shape[0],valores[i][60])
#         ds86 =np.insert(ds86,ds86.shape[0],valores[i][61])
#         hdh8 =np.insert(hdh8,hdh8.shape[0],valores[i][62]) 
#         tdh8 =np.insert(tdh8,tdh8.shape[0],valores[i][63])
#         
#         ds91 =np.insert(ds91,ds91.shape[0],valores[i][64])
#         ds92 =np.insert(ds92,ds92.shape[0],valores[i][65]) 
#         ds93 =np.insert(ds93,ds93.shape[0],valores[i][66]) 
#         ds94 =np.insert(ds94,ds94.shape[0],valores[i][67])
#         ds95 =np.insert(ds95,ds95.shape[0],valores[i][68])
#         ds96 =np.insert(ds96,ds96.shape[0],valores[i][69])  
#         hdh9 =np.insert(hdh9,hdh9.shape[0],valores[i][70]) 
#         tdh9 =np.insert(tdh9,tdh9.shape[0],valores[i][71])
    #print(psg0)
    #print(psg1)
    siu = True

    dsmean11 = np.mean([ds11[len(ds11)-1],ds12[len(ds12)-1],ds13[len(ds13)-1],ds14[len(ds14)-1],ds15[len(ds15)-1],ds16[len(ds16)-1],ds17[len(ds17)-1],ds18[len(ds18)-1],ds19[len(ds19)-1],ds110[len(ds110)-1],ds111[len(ds111)-1],ds112[len(ds112)-1]])    
    tamb = " "+str("%.1f" % np.mean([tdh1[len(tdh1)-1],[tdh2[len(tdh2)-1]]]))+" °C "
    hamb = str("%.1f" % np.mean([hdh1[len(hdh1)-1],[hdh2[len(hdh2)-1]]]))+" %"
    tfer = str("%.1f" % dsmean11)+" °C"# dsmean1[len(hdh1)-1])+" °C"
    
    window.Element('Tamb').Update(tamb)
    window.Element('Hamb').Update(hamb)
    window.Element('Tfer').Update(tfer)


def draw_plot1():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()
   
    pltds1, = ax1.plot(keys,ds11,color='#08090b',label="Temp 1", linewidth=2)
    pltds2, = ax1.plot(keys,ds12,color='#431f1d',label="Temp 2", linewidth=2)
    pltds3, = ax1.plot(keys,ds13,color='#90584b',label="Temp 3", linewidth=2)
    pltds4, = ax1.plot(keys,ds14,color='#c6783c',label="Temp 4", linewidth=2)
    pltds5, = ax1.plot(keys,ds15,color='#ebc6a8',label="Temp 5", linewidth=2)
    pltds6, = ax1.plot(keys,ds16,color='#5c4435',label="Temp 6", linewidth=2)
    pltds7, = ax1.plot(keys,ds17,color='#867167',label="Temp 7", linewidth=2)
    pltds8, = ax1.plot(keys,ds18,color='#af937a',label="Temp 8", linewidth=2)
    pltds9, = ax1.plot(keys,ds19,color='#c6b391',label="Temp 9", linewidth=2)
    pltds10, = ax1.plot(keys,ds110,color='#cbc1b4',label="Temp 10", linewidth=2)
    pltds11, = ax1.plot(keys,ds111,color='#90584b',label="Temp 11", linewidth=2)
    pltds12, = ax1.plot(keys,ds112,color='#c6783c',label="Temp 12", linewidth=2)
    plt.tight_layout(rect=[0,0.1,0.95,0.99])

    if(incluir==True):
        pltdh, =ax1.plot(keys,tdh1,'#fac369',label="T ambiente 1", linewidth=4,
         linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')
        pltdh1, =ax1.plot(keys,tdh2,'#fac369',label="T ambiente 2", linewidth=4,
         linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')

    ax1.set_xlabel('Tiempo', fontsize=12)
    ax1.set_ylabel('Temperatura[°C]', fontsize=12)
    ax1.set_ylim(15,65)
    ax1.yaxis.label.set_color(pltds3.get_color())
    ax1.tick_params(axis='y', colors=pltds3.get_color())
    if(incluir==True):
        pltax2, = ax2.plot(keys,hdh1,'#00aea5', label="H Ambiente 1", linewidth=4,
         linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')
        pltax3, = ax2.plot(keys,hdh2,'#00aea5', label="H Ambiente 2", linewidth=4,
         linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')
   #     ax2.errorbar(keys, hdh1,color='#00aea6', yerr=0.1, uplims=True, lolims=True,
   #          label='uplims=True, lolims=True')
        ax2.set_ylabel('Humedad [%]', fontsize=12)
        ax2.set_ylim(20,100)
        ax2.yaxis.label.set_color(pltax2.get_color())
        ax2.spines['left'].set_color(pltds3.get_color())
        ax2.spines['right'].set_color(pltax2.get_color())
        ax2.tick_params(axis='y', colors=pltax2.get_color())

        plt.legend((pltdh,pltdh1,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltds7,pltds8,pltds9,pltds10,pltds11,pltds12,pltax2,pltax3),("T ambiente 1","T ambiente 2","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","Temp 7","Temp 8","Temp 9","Temp 10","Temp 11","Temp 12","H Ambiente 1", "H Ambiente 2"),prop = {'size': 12},loc='center left', bbox_to_anchor=(1.04,0.5)
                                              , fancybox=True, shadow=True)
    else:
        plt.legend((pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltds7,pltds8,pltds9,pltds10,pltds11,pltds12),("Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","Temp 7","Temp 8","Temp 9","Temp 10","Temp 11","Temp 12"),prop = {'size': 12},loc='center left', bbox_to_anchor=(1.04,0.5)
                                              , fancybox=True, shadow=True)

    plt.title('Comportamiento Fermentador 1', fontsize=15)

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)

    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F1.png", bbox_inches="tight")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
def draw_plot2():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltds1, = ax1.plot(keys,ds21,label="Temp 1")
    pltds2, = ax1.plot(keys,ds22,label="Temp 2")
    pltds3, = ax1.plot(keys,ds23,label="Temp 3")
    pltds4, = ax1.plot(keys,ds24,label="Temp 4")
    pltds5, = ax1.plot(keys,ds25,label="Temp 5")
    pltds6, = ax1.plot(keys,ds26,label="Temp 6")
    
    if(incluir==True):
        pltdh, =ax1.plot(keys,tdh2,label="T ambiente")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh2,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.legend((pltdh,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltax2),("T ambiente","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","H Ambiente"),prop = {'size': 8}, loc='upper right')
    plt.title('Comportamiento Fermentador 2')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F2.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
    
def draw_plot3():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltdh, =ax1.plot(keys,tdh3,label="T ambiente")
    pltds1, = ax1.plot(keys,ds31,label="Temp 1")
    pltds2, = ax1.plot(keys,ds32,label="Temp 2")
    pltds3, = ax1.plot(keys,ds33,label="Temp 3")
    pltds4, = ax1.plot(keys,ds34,label="Temp 4")
    pltds5, = ax1.plot(keys,ds35,label="Temp 5")
    pltds6, = ax1.plot(keys,ds36,label="Temp 6")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh3,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.legend((pltdh,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltax2),("T ambiente","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","H Ambiente"),prop = {'size': 8}, loc='upper right')
    plt.title('Comportamiento Fermentador 3')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F3.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
    
def draw_plot4():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltdh, =ax1.plot(keys,tdh4,label="T ambiente")
    pltds1, = ax1.plot(keys,ds41,label="Temp 1")
    pltds2, = ax1.plot(keys,ds42,label="Temp 2")
    pltds3, = ax1.plot(keys,ds43,label="Temp 3")
    pltds4, = ax1.plot(keys,ds44,label="Temp 4")
    pltds5, = ax1.plot(keys,ds45,label="Temp 5")
    pltds6, = ax1.plot(keys,ds46,label="Temp 6")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh4,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.title('Comportamiento Fermentador 4')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F4.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
def draw_plot5():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltdh, =ax1.plot(keys,tdh5,label="T ambiente")
    pltds1, = ax1.plot(keys,ds51,label="Temp 1")
    pltds2, = ax1.plot(keys,ds52,label="Temp 2")
    pltds3, = ax1.plot(keys,ds53,label="Temp 3")
    pltds4, = ax1.plot(keys,ds54,label="Temp 4")
    pltds5, = ax1.plot(keys,ds55,label="Temp 5")
    pltds6, = ax1.plot(keys,ds56,label="Temp 6")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh5,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.legend((pltdh,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltax2),("T ambiente","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","H Ambiente"),prop = {'size': 8}, loc='upper right')
    plt.title('Comportamiento Fermentador 5')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F5.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
def draw_plot6():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltdh, =ax1.plot(keys,tdh6,label="T ambiente")
    pltds1, = ax1.plot(keys,ds61,label="Temp 1")
    pltds2, = ax1.plot(keys,ds62,label="Temp 2")
    pltds3, = ax1.plot(keys,ds63,label="Temp 3")
    pltds4, = ax1.plot(keys,ds64,label="Temp 4")
    pltds5, = ax1.plot(keys,ds65,label="Temp 5")
    pltds6, = ax1.plot(keys,ds66,label="Temp 6")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh6,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.legend((pltdh,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltax2),("T ambiente","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","H Ambiente"),prop = {'size': 8}, loc='upper right')
    plt.title('Comportamiento Fermentador 6')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F6.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
def draw_plot7():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltdh, =ax1.plot(keys,tdh7,label="T ambiente")
    pltds1, = ax1.plot(keys,ds71,label="Temp 1")
    pltds2, = ax1.plot(keys,ds72,label="Temp 2")
    pltds3, = ax1.plot(keys,ds73,label="Temp 3")
    pltds4, = ax1.plot(keys,ds74,label="Temp 4")
    pltds5, = ax1.plot(keys,ds75,label="Temp 5")
    pltds6, = ax1.plot(keys,ds76,label="Temp 6")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh7,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.legend((pltdh,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltax2),("T ambiente","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","H Ambiente"),prop = {'size': 8}, loc='upper right')
    plt.title('Comportamiento Fermentador 7')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F7.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
def draw_plot8():
    fig = plt.figure()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltdh, =ax1.plot(keys,tdh8,label="T ambiente")
    pltds1, = ax1.plot(keys,ds81,label="Temp 1")
    pltds2, = ax1.plot(keys,ds82,label="Temp 2")
    pltds3, = ax1.plot(keys,ds83,label="Temp 3")
    pltds4, = ax1.plot(keys,ds84,label="Temp 4")
    pltds5, = ax1.plot(keys,ds85,label="Temp 5")
    pltds6, = ax1.plot(keys,ds86,label="Temp 6")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh8,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.legend((pltdh,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltax2),("T ambiente","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","H Ambiente"),prop = {'size': 8}, loc='upper right')
    plt.title('Comportamiento Fermentador 8')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F8.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
def draw_plot9():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltdh, =ax1.plot(keys,tdh9,label="T ambiente")
    pltds1, = ax1.plot(keys,ds91,label="Temp 1")
    pltds2, = ax1.plot(keys,ds92,label="Temp 2")
    pltds3, = ax1.plot(keys,ds93,label="Temp 3")
    pltds4, = ax1.plot(keys,ds94,label="Temp 4")
    pltds5, = ax1.plot(keys,ds95,label="Temp 5")
    pltds6, = ax1.plot(keys,ds96,label="Temp 6")

    # ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    #  plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo [HH:MM:SS]')
    ax1.set_ylabel('Temperatura[°C]')
    pltax2, = ax2.plot(keys,hdh9,'g',label="H Ambiente")
    ax2.set_ylabel('Humedad [%]')

    ax1.set_ylim(10,50)
    ax2.set_ylim(20,100)
    plt.legend((pltdh,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltax2),("T ambiente","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","H Ambiente"),prop = {'size': 8}, loc='upper right')
    plt.title('Comportamiento Fermentador 9')

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()

   
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)
    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F9.png")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
def draw_rend():
   
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.clear()
    ax2.clear()

    pltds1, = ax1.plot(diitas,dsd11,color='#08090b',label="Temp 1", linewidth=2)
    #ax1.errorbar(keys, ds11,color='#08090b', yerr=0.01, uplims=True, lolims=True,
   #          label='uplims=True, lolims=True')
    pltds2, = ax1.plot(diitas,dsd12,color='#431f1d',label="Temp 2", linewidth=2)
    #ax1.errorbar(keys, ds12,color='#431f1d', yerr=0.01, uplims=True, lolims=True,
    #         label='uplims=True, lolims=True')
    pltds3, = ax1.plot(diitas,dsd13,color='#90584b',label="Temp 3", linewidth=2)
    #ax1.errorbar(keys, ds13,color='#90584b', yerr=0.01, uplims=True, lolims=True,
    #         label='uplims=True, lolims=True')
    pltds4, = ax1.plot(diitas,dsd14,color='#c6783c',label="Temp 4", linewidth=2)
   # ax1.errorbar(keys, ds14,color='#c6783c', yerr=0.01, uplims=True, lolims=True,
    #         label='uplims=True, lolims=True')
    pltds5, = ax1.plot(diitas,dsd15,color='#ebc6a8',label="Temp 5", linewidth=2)
    #ax1.errorbar(keys, ds15,color='#ebc6a8', yerr=0.01, uplims=True, lolims=True,
    #         label='uplims=True, lolims=True')
    pltds6, = ax1.plot(diitas,dsd16,color='#5c4435',label="Temp 6", linewidth=2)
    #ax1.errorbar(keys, ds16,color='#5c4435', yerr=0.01, uplims=True, lolims=True,
    #         label='uplims=True, lolims=True')
    pltds7, = ax1.plot(diitas,dsd17,color='#867167',label="Temp 7", linewidth=2)
   # ax1.errorbar(keys, ds17,color='#867167', yerr=0.01, uplims=True, lolims=True,
    #         label='uplims=True, lolims=True')
    pltds8, = ax1.plot(diitas,dsd18,color='#af937a',label="Temp 8", linewidth=2)
    #ax1.errorbar(keys, ds18,color='#af937a', yerr=0.01, uplims=True, lolims=True,
    #         label='uplims=True, lolims=True')
    pltds9, = ax1.plot(diitas,dsd19,color='#c6b391',label="Temp 9", linewidth=2)
   # ax1.errorbar(keys, ds19,color='#c6b391', yerr=0.01, uplims=True, lolims=True,
   #          label='uplims=True, lolims=True')
    pltds10, = ax1.plot(diitas,dsd110,color='#cbc1b4',label="Temp 10", linewidth=2)
   # ax1.errorbar(keys, ds110,color='#cbc1b4', yerr=0.01, uplims=True, lolims=True,
     #        label='uplims=True, lolims=True')
    pltds11, = ax1.plot(diitas,dsd111,color='#90584b',label="Temp 11", linewidth=2)
    #ax1.errorbar(keys, ds111,color='#90584b', yerr=0.01, uplims=True, lolims=True,
     #        label='uplims=True, lolims=True')
    pltds12, = ax1.plot(diitas,dsd112,color='#c6783c',label="Temp 12", linewidth=2)
    #ax1.errorbar(keys, ds112,color='#c6783c', yerr=0.01, uplims=True, lolims=True,
     #        label='uplims=True, lolims=True')
    plt.tight_layout(rect=[0,0.1,0.95,0.99])

    if(incluir==True):
        pltdh, =ax1.plot(diitas,tdhd1,'#fac369',label="T ambiente 1", linewidth=4,
        linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')
        pltdh1, =ax1.plot(diitas,tdhd2,'#fac369',label="T ambiente 1", linewidth=4,
        linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')
       # ax1.errorbar(keys, tdh1,color='#fac368', yerr=0.1, uplims=True, lolims=True,
       #      label='uplims=True, lolims=True')
           
    #ax1.legend(("LM35","T DHT11","DS18B20"),prop = {'size': 10}, loc='upper right')

    plt.legend(prop = {'size': 10}, loc='upper right')
    ax1.set_xlabel('Tiempo', fontsize=12)
    ax1.set_ylabel('Temperatura[°C]', fontsize=12)
    ax1.set_ylim(15,65)
    ax1.yaxis.label.set_color(pltds3.get_color())
    ax1.tick_params(axis='y', colors=pltds3.get_color())
    if(incluir==True):
        pltax2, = ax2.plot(diitas,hdhd1,'#00aea5', label="H Ambiente 1", linewidth=4,
         linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')
        pltax3, = ax2.plot(diitas,hdhd2,'#00aea5', label="H Ambiente 2", linewidth=4,
         linestyle=(0, (3, 1, 1, 2)), dash_capstyle='round')
      #  ax2.errorbar(keys, hdh1,color='#00aea6', yerr=0.1, uplims=True, lolims=True,
      #       label='uplims=True, lolims=True')
        ax2.set_ylabel('Humedad [%]', fontsize=12)
        ax2.set_ylim(20,100)
        ax2.yaxis.label.set_color(pltax2.get_color())
        ax2.spines['left'].set_color(pltds3.get_color())
        ax2.spines['right'].set_color(pltax2.get_color())
        ax2.tick_params(axis='y', colors=pltax2.get_color())

        plt.legend((pltdh,pltdh1,pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltds7,pltds8,pltds9,pltds10,pltds11,pltds12,pltax2,pltax3),("T ambiente","T ambiente 2","Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","Temp 7","Temp 8","Temp 9","Temp 10","Temp 11","Temp 12","H Ambiente 1","H Ambiente 2"),prop = {'size': 12},loc='center left', bbox_to_anchor=(1.04,0.5)
                                             , fancybox=True, shadow=True)
    else:
        plt.legend((pltds1,pltds2,pltds3,pltds4,pltds5,pltds6,pltds7,pltds8,pltds9,pltds10,pltds11,pltds12),("Temp 1","Temp 2","Temp 3","Temp 4","Temp 5","Temp 6","Temp 7","Temp 8","Temp 9","Temp 10","Temp 11","Temp 12"),prop = {'size': 12},loc='center left', bbox_to_anchor=(1.04,0.5)
                                              , fancybox=True, shadow=True)

    plt.title('Comportamiento Fermentadores', fontsize=15)

    plt.grid()
    #plt.xlabel('Tiempo [s]')
    #  p1,p2,p3,p4 = plt.plot(keys,tlm, keys, hdh, keys, tdh, keys, tds)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.pause(0.05)

    plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"FRendimiento.png", bbox_inches="tight")
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()
    
w,h=sg.Window.get_screen_size()
    
layout = [
    [ sg.Text('', size=(300, 1), justification='center', font=("Helvetica", 5)),sg.Button('X', key='cerrar',size=(2, 1),font=("Helvetica", 5))],
    [sg.Image('/home/pi/Raspduino/bio1.png'),sg.Text('Mapeo Fermentación',  size=(25, 1), justification='center', font=("Helvetica", 30))],
    [sg.Text('═' * 210, font=("Helvetica", 8))],  
    [sg.Text('',key='lectura',  size=(40, 1), justification='center', font=("Helvetica", 10)), sg.Text('', size=(5, 1)),sg.Button('Iniciar', button_color='white on green',key='inicio',size=(10, 1),font=("Helvetica", 9)),  sg.Text('Día #', key='dia',size=(20, 1), justification='center', font=("Helvetica", 25)),sg.Button('Finalizar', button_color='white on red', key='fin',size=(10, 1),font=("Helvetica", 9))],
     [sg.Text('═' * 210, font=("Helvetica", 8))],
    [sg.Text('Condiciones Ambientales', size=(34, 1), justification='center', font=("Helvetica", 23)),
     sg.Text('', size=(6,1), justification='center', font=("Helvetica", 10)),
     sg.Text('Fermentador', size=(34, 1), justification='center', font=("Helvetica", 23))],
    [sg.Text('  --  °C ',  key = 'Tamb',size=(6, 1), justification='center', font=("Helvetica", 60)),
     sg.Text(' ', size=(2, 1), justification='center', font=("Helvetica", 20)),
     sg.Text('  --  %', size=(6, 1), justification='center', font=("Helvetica", 60), key='Hamb'),
      sg.Text(' ', size=(4, 1), justification='center', font=("Helvetica", 40)),
     sg.Text(' --  °C', size=(6, 1), justification='center', font=("Helvetica", 90),key='Tfer')], #, relief=sg.RELIEF_RIDGE
       [sg.Text('Temperatura', size=(28, 1), justification='center', font=("Helvetica", 14)),
        sg.Text('Humedad', size=(28, 1), justification='center', font=("Helvetica", 14)),
     sg.Text('', size=(22, 1), justification='center', font=("Helvetica", 10)),
     sg.Text('Temperatura Promedio', size=(38, 1), justification='center', font=("Helvetica", 14))],#
        [sg.Text('═' * 210, font=("Helvetica", 8))],


#     sg.Multiline(default_text='A second multi-line', size=(35, 3))],


   [sg.Text('Gráficas',font=("Helvetica", 15)),sg.Text('', size=(85, 1))],
        [sg.Checkbox('Incluir datos ambientales', key = 'checkamb',size=(50,1), default=True,font=("Helvetica", 10))],
    [sg.InputCombo(('Fermentador 1',),size=(40, 10),font=("Helvetica", 13),key='combofer'), # 'Fermentador 2', 'Fermentador 3','Fermentador 4', 'Fermentador 5', 'Fermentador 6','Fermentador 7', 'Fermentador 8', 'Fermentador 9'
     #sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
   # [sg.InputOptionMenu(('Fermentador 1', 'Fermentador 2', 'Fermentador 3','Fermentador 4', 'Fermentador 5', 'Fermentador 6'),size=(100, 20))],
    #[sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3', 'Fermentador 3','Fermentador 4', 'Fermentador 5'), size=(30, 3)),
     
    sg.Button('Graficar', key='buttongraficar',size=(13, 1),font=("Helvetica", 13)),
    
    sg.Text('', size=(20, 1),font=("Helvetica", 10)),
    
    # [sg.Frame('Labelled Group',[[
    # sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
    # sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
    # sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
    # sg.Column(column1, background_color='lightblue')]])],
        
        sg.Text('', size=(2, 1)),sg.Button('Mostrar desempeño semanal', key='buttondesempeño',size=(30, 1),font=("Helvetica", 13))],
           [sg.Text('═' * 210, font=("Helvetica", 8))],
        [sg.Text('Registro de eventos',font=("Helvetica", 15)),sg.Text('',font=("Helvetica", 11), size=(27, 1)),sg.Button('Guardar Evento',button_color='white on black', key='buttonnota',size=(20, 1),font=("Helvetica", 10)),sg.Text('',font=("Helvetica", 10), size=(12, 1)),sg.Text('Ubicación de datos',font=("Helvetica", 15))],
  #  [sg.Frame(layout=[
  #  [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],
#    [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Multiline(default_text='Escribir apuntes del proceso', key='multiline',size=(71, 4),font=("Helvetica", 11)),
     sg.Text('', size=(8, 1),font=("Helvetica", 15)),sg.Input(default_text=rutaglobal,key='fileinput',size=(40, 1),font=("Helvetica", 11)),sg.Text('', size=(3, 1)),sg.Button('Cambiar Ubicación', key='buttonfile',size=(15, 1),font=("Helvetica", 11))],
             [sg.Text('═' * 210, font=("Helvetica", 8))]]
window = sg.Window('Control Ambiental Fermentación', layout, location=(0,0), size=(w,h), resizable=True,finalize=True)
#window.Maximize()

var=False
arranque = False
act=False
aviso =0
rutan = rutaglobal+"/notas"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".txt"
outFile=open(rutan, "a")
while True:

    
    event, values = window.read(timeout = 10)
    

    if event == 'inicio':
        outFile=open(rutan, "a")
        arranque= True
        contdia = datetime.now() #- timedelta(days=7)
    if not(values is None):
        checkamb =values['checkamb']
    if checkamb:
        incluir = True
    else:
        incluir = False
    if((var==False and contador>0)and act==False):
            window.Element('lectura').Update('')
            act=True
    if (((((int(time.time()-instanteInicial))/60)>1.1) or contador==0)and arranque==True):
        #comando = raw_input('Introduce un comando: ') #Input
        #arduino.write(comando) #Mandar un comando hacia Arduino
        if(contador==0):
            window.Element('lectura').Update('Sin datos')
        instanteInicial = time.time()
        dif = datetime.now()-contdia
        dias = dif.days
        window.Element('dia').Update('Día # ' +str(dias))
        arduino1.write(str.encode("SIU"))
        print("Escribiendo")
        contador = contador+1
        var = True

#         arduino2.write(str.encode('S'))
#         arduino3.write(str.encode('S'))
#         arduino4.write(str.encode('S'))
#         arduino5.write(str.encode('S'))
#         arduino6.write(str.encode('S'))
#         arduino7.write(str.encode('S'))
#         arduino8.write(str.encode('S'))
#         arduino9.write(str.encode('S'))
#     if(contador>1):
#         plt.ion()

    if ((((time.time()-instanteInicial)/60)>0.9) and var==True):
        window.Element('lectura').Update('En lectura')
    if (((((time.time()-instanteInicial))/60)>0.93) and var==True):
        print("Leyendo")
        
        lecturadatos()
        var= False
        act=False
    if event == 'buttonnota':
        nota = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+"  "+values['multiline']
        outFile.write(nota)
        window.Element('multiline').Update('')
        sg.popup_timed('Nota Guardada', 'Su nota fue almacenada en la ubicación elegida!',keep_on_top=True)

        
    if event == 'buttonfile':
       folder=  sg.popup_get_folder('Porfavor ingrese una nueva ubicación')
       if folder == 'OK':
           rutaglobal = folder
           window.Element('fileinput').Update(rutaglobal)
           rutan = rutaglobal+"/notas"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".txt"
           outFile.close()
           outFile=open(rutan, "a")

       
    if dias >14:
        aviso += 1
    
    
    if (event == 'fin' or aviso==1) or (event in (sg.WIN_CLOSED, 'cerrar')):       
        seg= sg.popup_ok_cancel('¿Está seguro de finalizar la lectura de datos?',keep_on_top=True)  # Shows OK and Cancel buttons
        if seg == 'OK':
            print('fin')
            window.Element('dia').Update('Día # ')
            window.Element('lectura').Update('')
            window.Element('Tamb').Update('  --  °C ')
            window.Element('Hamb').Update('  --  %')
            window.Element('Tfer').Update(' --  °C')
            outFile.close()
            arranque= False
            contador=0
            var=False
            if len(hdh1)!=0:
                df= pd.DataFrame([key for key in psg.keys()], columns=['Fecha y hora'])
                df['H ambiente 1'] = hdh1
                df['T ambiente 1'] = tdh1
                df['H ambiente 2'] = hdh2
                df['T ambiente 2'] = tdh2
                df['Temp 11'] = ds11
                df['Temp 12'] = ds12
                df['Temp 13'] = ds13
                df['Temp 14'] = ds14
                df['Temp 15'] = ds15
                df['Temp 16'] = ds16
                df['Temp 17'] = ds17
                df['Temp 18'] = ds18
                df['Temp 19'] = ds19
                df['Temp 110'] = ds110
                df['Temp 111'] = ds111
                df['Temp 112'] = ds112
        #         df['Temp 21'] = ds21
        #         df['Temp 22'] = ds22
        #         df['Temp 23'] = ds23
        #         df['Temp 24'] = ds24
        #         df['Temp 25'] = ds25
        #         df['Temp 26'] = ds26
        #         df['Temp 31'] = ds31
        #         df['Temp 32'] = ds32
        #         df['Temp 33'] = ds33
        #         df['Temp 34'] = ds34
        #         df['Temp 35'] = ds35
        #         df['Temp 36'] = ds36
        #         df['Temp 41'] = ds41
        #         df['Temp 42'] = ds42
        #         df['Temp 43'] = ds43
        #         df['Temp 44'] = ds44
        #         df['Temp 45'] = ds45
        #         df['Temp 46'] = ds46
        #         df['Temp 51'] = ds51
        #         df['Temp 52'] = ds52
        #         df['Temp 53'] = ds53
        #         df['Temp 54'] = ds54
        #         df['Temp 55'] = ds55
        #         df['Temp 56'] = ds56
        #         df['Temp 61'] = ds61
        #         df['Temp 62'] = ds62
        #         df['Temp 63'] = ds63
        #         df['Temp 64'] = ds64
        #         df['Temp 65'] = ds65
        #         df['Temp 66'] = ds66
        #         df['Temp 71'] = ds71
        #         df['Temp 72'] = ds72
        #         df['Temp 73'] = ds73
        #         df['Temp 74'] = ds74
        #         df['Temp 75'] = ds75
        #         df['Temp 76'] = ds76
        #         df['Temp 81'] = ds81
        #         df['Temp 82'] = ds82
        #         df['Temp 83'] = ds83
        #         df['Temp 84'] = ds84
        #         df['Temp 85'] = ds85
        #         df['Temp 86'] = ds86
        #         df['Temp 91'] = ds91
        #         df['Temp 92'] = ds92
        #         df['Temp 93'] = ds93
        #         df['Temp 94'] = ds94
        #         df['Temp 95'] = ds95
        #         df['Temp 96'] = ds96
        #    
                ruta1 = rutaglobal+"/datos"+datei.strftime("%m-%d-%Y-%H:%M:%S")+".xlsx"
                df2= pd.DataFrame(diitas, columns=['Día de Fermentación'])
             
                df2['H ambiente 1'] = hdhd1 
                df2['T ambiente 1'] = tdhd1
                df2['H ambiente 2'] = hdhd2
                df2['T ambiente 2'] = hdhd2
                df2['Temp 11'] = dsd11
                df2['Temp 12'] = dsd12
                df2['Temp 13'] = dsd13
                df2['Temp 14'] = dsd14
                df2['Temp 15'] = dsd15
                df2['Temp 16'] = dsd16
                df2['Temp 17'] = dsd17
                df2['Temp 18'] = dsd18
                df2['Temp 19'] = dsd19
                df2['Temp 110'] = dsd110
                df2['Temp 111'] = dsd111
                df2['Temp 112'] = dsd112
                writer = pd.ExcelWriter(ruta1, engine = 'openpyxl')
                df.to_excel(writer, sheet_name='Total_Datos_Fermentacion')
                df2.to_excel(writer, sheet_name='Rendimiento Semanal')
                writer.save()
                writer.close()             #ruta1 = "/Users/SANTIAGO/Desktop/SANTIAGO/Uniandes/Maestría/Temperatura/Agua Calentador 2/rutaa.xlsx"
            ds11 = np.zeros((0,1))
            ds12 = np.zeros((0,1))
            ds13 = np.zeros((0,1))
            ds14 = np.zeros((0,1))
            ds15 = np.zeros((0,1))
            ds16 = np.zeros((0,1))
            ds17 = np.zeros((0,1))
            ds18 = np.zeros((0,1))
            ds19 = np.zeros((0,1))
            ds110 = np.zeros((0,1))
            ds111 = np.zeros((0,1))
            ds112 = np.zeros((0,1))
            hdh1 = np.zeros((0,1))
            tdh1 = np.zeros((0,1))

            hdhd1 = np.zeros((14,))
            tdhd1 = np.zeros((14,))
            hdhd2 = np.zeros((14,))
            tdhd2 = np.zeros((14,))
            dsd11 = np.zeros((14,))
            dsd12 = np.zeros((14,))
            dsd13 = np.zeros((14,))
            dsd14 = np.zeros((14,))
            dsd15 = np.zeros((14,))
            dsd16 = np.zeros((14,))
            dsd17 = np.zeros((14,))
            dsd18 = np.zeros((14,))
            dsd19 = np.zeros((14,))
            dsd110 = np.zeros((14,))
            dsd111 = np.zeros((14,))
            dsd112 = np.zeros((14,))
            ds21 = np.zeros((0,1))
            ds22 = np.zeros((0,1))
            ds23 = np.zeros((0,1))
            ds24 = np.zeros((0,1))
            ds25 = np.zeros((0,1))
            ds26 = np.zeros((0,1))
            hdh2 = np.zeros((0,1))
            tdh2 = np.zeros((0,1))

            ds31 = np.zeros((0,1))
            ds32 = np.zeros((0,1))
            ds33 = np.zeros((0,1))
            ds34 = np.zeros((0,1))
            ds35 = np.zeros((0,1))
            ds36 = np.zeros((0,1))
            hdh3 = np.zeros((0,1))
            tdh3 = np.zeros((0,1))

            ds41 = np.zeros((0,1))
            ds42 = np.zeros((0,1))
            ds43 = np.zeros((0,1))
            ds44 = np.zeros((0,1))
            ds45 = np.zeros((0,1))
            ds46 = np.zeros((0,1))
            hdh4 = np.zeros((0,1))
            tdh4 = np.zeros((0,1))

            ds51 = np.zeros((0,1))
            ds52 = np.zeros((0,1))
            ds53 = np.zeros((0,1))
            ds54 = np.zeros((0,1))
            ds55 = np.zeros((0,1))
            ds56 = np.zeros((0,1))
            hdh5 = np.zeros((0,1))
            tdh5 = np.zeros((0,1))

            ds61 = np.zeros((0,1))
            ds62 = np.zeros((0,1))
            ds63 = np.zeros((0,1))
            ds64 = np.zeros((0,1))
            ds65 = np.zeros((0,1))
            ds66 = np.zeros((0,1))
            hdh6 = np.zeros((0,1))
            tdh6 = np.zeros((0,1))

            ds71 = np.zeros((0,1))
            ds72 = np.zeros((0,1))
            ds73 = np.zeros((0,1))
            ds74 = np.zeros((0,1))
            ds75 = np.zeros((0,1))
            ds76 = np.zeros((0,1))
            hdh7 = np.zeros((0,1))
            tdh7 = np.zeros((0,1))

            ds81 = np.zeros((0,1))
            ds82 = np.zeros((0,1))
            ds83 = np.zeros((0,1))
            ds84 = np.zeros((0,1))
            ds85 = np.zeros((0,1))
            ds86 = np.zeros((0,1))
            hdh8 = np.zeros((0,1))
            tdh8 = np.zeros((0,1))

            ds91 = np.zeros((0,1))
            ds92 = np.zeros((0,1))
            ds93 = np.zeros((0,1))
            ds94 = np.zeros((0,1))
            ds95 = np.zeros((0,1))
            ds96 = np.zeros((0,1))
            hdh9 = np.zeros((0,1))
            tdh9 = np.zeros((0,1))
            if event in (sg.WIN_CLOSED, 'cerrar'):
                arduino1.close() #Finalizamos la comunicacion
#               arduino2.close() #Finalizamos la comunicacion
#         arduino3.close() #Finalizamos la comunicacion
#         arduino4.close() #Finalizamos la comunicacion
#         arduino5.close() #Finalizamos la comunicacion
#         arduino6.close() #Finalizamos la comunicacion
#         arduino7.close() #Finalizamos la comunicacion
#         arduino8.close() #Finalizamos la comunicacion
#         arduino9.close() #Finalizamos la comunicacion

                break    


   
    if event == 'buttongraficar':
        if (values['combofer'] == 'Fermentador 1'):  
            draw_plot1()
        if (values['combofer'] == 'Fermentador 2'):  
            draw_plot2()
        if (values['combofer'] == 'Fermentador 3'):  
            draw_plot3()
        if (values['combofer'] == 'Fermentador 4'):  
            draw_plot4()
        if (values['combofer'] == 'Fermentador 5'):  
            draw_plot5()
        if (values['combofer'] == 'Fermentador 6'):  
            draw_plot6()
        if (values['combofer'] == 'Fermentador 7'):  
            draw_plot7()
        if (values['combofer'] == 'Fermentador 8'):  
            draw_plot8()
        if (values['combofer'] == 'Fermentador 9'):  
            draw_plot9()
            
    if event == 'buttondesempeño':
        draw_rend()
#     elif event == 'button':  
#         sg.Popup('Title',
#                  'The results of the window.',
#                  'The button clicked was "{}"'.format(event),
#                  'The values are', values)
#     elif event.startswith('max'):
#         window.Maximize()
#     elif event.startswith('Escape'):
#         window.normal()
window.close()
        
        

