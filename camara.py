import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime as dt # Se usa para guardar las imagenes

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate



def TakePicture(ruta, nombre):
    frame = np.zeros((24*32,)) # Inicialización del tamaño de la imagen, en total 768 pts en un vector de 1xn
    mlx.getFrame(frame) # Se actualiza el vector frame con los datos de la camara

    mlx_shape = (24,32) # Tamaño real de la imagen mlx90640 shape en forma de matriz
    data_array = np.fliplr(np.reshape(frame,mlx_shape)) # Actualización del frame en data_frame, ahora es una matriz con los datos de la imagen


    fig =plt.figure() # Se crea una figura
    ax=fig.add_subplot(111) # Se crea un subplot (Necesario para agregar textos, colorbar, ext.)
    N = 26
    mean = np.mean(frame) # Se obtiene temperatura media
    textstr = "Mean temperature: " + str(mean) + "°C" # Se crea el texto que acompañará a la imagen  
    props = dict(boxstyle="round", facecolor = "wheat", alpha = 0.5) # estilo de la caja de texto
    t1 = ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize = 14, fontstyle =  "italic",verticalalignment = "top", bbox = props) # Se crea una caja de texto
    cmap=plt.get_cmap('jet',26) # Estilo de la barra de color
    therm1 = ax.imshow(data_array,interpolation='none', cmap=cmap,vmin=10,vmax=60) # Se coloca la imagen del data_array en la figura
    cbar = fig.colorbar(therm1, ticks=np.linspace(10, 260, N), label = "Temperature [°C]") # Se establece la barra de color
    # Ahora se definen el titulo y los ejes
    plt.title(label="Thermal view",
          position=(0.5, 0.9),
          fontdict={'family': 'Dejavu Serif',
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16})

    plt.xlabel("x-coordinate", size = 12)
    plt.ylabel("y-coordinate", size = 12)

    # Finalmente se guarda como imagen en la ruta por parametro
    fig.savefig(str(ruta) + str(nombre) + ".png")
