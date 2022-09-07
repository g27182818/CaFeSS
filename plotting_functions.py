import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import pandas as pd
import os
from matplotlib import cm
import scipy.interpolate as interp
import matplotlib



def plot_fermenter_sensors(ferementer, global_df, resample):
    """
    This function plots all the sensors of a given fermenter resampled by time. It also plots ambient temperature and humidity.

    Args:
        fermenter (int): The fermenter to plot. Only positive integers.
        global_df (pandas.DataFrame): Dataframe with all required information
        resample (str): String specifying the frequency to resample data. Cannot be less than the original sampling frequency.
    """
    # Get specific fermenter data
    fermenter_df = global_df[f'f{ferementer}'].resample(resample).mean()
    fermenter_df = fermenter_df.add_prefix('Sensor ')
    fermenter_df.index.name, fermenter_df.columns.name = None, None
    # Get ambient temperature data
    t_amb_df = global_df['t_amb'].resample(resample).mean()
    t_amb_df = t_amb_df.add_prefix('T-amb ')
    t_amb_df.index.name, t_amb_df.columns.name = None, None

    # Get ambient humidity data
    h_amb_df = global_df['h_amb'].resample(resample).mean()
    h_amb_df = h_amb_df.add_prefix('H-amb ')
    h_amb_df.index.name, h_amb_df.columns.name = None, None

    # Plot ambient temperatures
    ax1 = t_amb_df.plot(figsize=(8, 6))

    # Plot Fermenters
    fermenter_df.plot( grid=True, title=f'Sensores de fermentador {ferementer}',
                        xlim = (fermenter_df.index.min(), fermenter_df.index.max()),
                        ylim = (10.0, 60.0),
                        xlabel='Fecha-Hora',
                        ylabel='Temperatura [$^oC$]',
                        ax=ax1)

    # Plot humidity data
    ax2 = plt.twinx()
    h_amb_df.plot(ylim = (10.0, 100.0),
                  ylabel='Humedad [%]',
                  ax=ax2)
    

    ax1.legend(loc='center left',bbox_to_anchor=(1.15, 0.5))
    ax2.legend()
    plt.tight_layout()

    #     figManager = plt.get_current_fig_manager()
    #     figManager.window.showMaximized()
    #     plt.savefig(rutaglobal+"/"+datetime.now().strftime("%m-%d-%Y-%H:%M:%S")+"F1.png", bbox_inches="tight")

    plt.show()

def plot_fermenter_average(fermenter, global_df, resample):
    """
    This function plots the averages of any fermenter resampled by time. It also plots ambient temperature and humidity.

    Args:
        fermenter (int): The fermenter to plot. -1 to plot al fermenters
        global_df (pandas.DataFrame): Dataframe with all required information
        resample (str): String specifying the frequency to resample data. Cannot be less than the original sampling frequency.
    """
    # Get averages of all sensors and ambient temperature
    average_df = global_df.groupby(level=0, axis=1).mean()
    
    # Get plot dataframes for ambient temperature and humidity
    t_amb_plot_df = average_df['t_amb'].resample(resample).mean()
    h_amb_plot_df = average_df['h_amb'].resample(resample).mean()
    
    # Handle to plot all fermenters or just one
    if fermenter == -1:
        # Case to plot all fermenters
        plot_df = average_df.iloc[:,average_df.columns.str.contains('f')].resample(resample).mean()
        plot_df.columns = plot_df.columns.str.replace('f', 'Ferm. ') # Set names for plot labels
        title_str = 'Promedio de todos los fermentadores cada '+resample
    else:
        # Case to plot just one fermenter
        plot_df = average_df[f'f{fermenter}'].resample(resample).mean()
        plot_df.name = f'Ferm. {fermenter}'
        title_str = f'Promedio de fermentador {fermenter} cada '+ resample


    # Plot ambient temperatures
    ax1 = t_amb_plot_df.plot(figsize=(8, 6), label='T-amb', style='--.k')

    # Plot Fermenters
    plot_df.plot( grid=True, title=title_str,
                        xlim = (plot_df.index.min(), plot_df.index.max()),
                        ylim = (10.0, 60.0),
                        xlabel='Fecha-Hora',
                        ylabel='Temperatura [$^oC$]',
                        ax=ax1,
                        style='--.')

    # Plot humidity data
    ax2 = plt.twinx()
    h_amb_plot_df.plot(ylim = (10.0, 100.0),
                  ylabel='Humedad [%]',
                  ax=ax2, label='H-amb', style='--.b')
    
    # Set legends of 
    ax1.legend(loc='center left',bbox_to_anchor=(1.15, 0.5))
    ax2.legend()
    plt.tight_layout()
    plt.show()

def plot_fermenter_boxplot(fermenter, global_df):
    """
    This function plots boxplots for the measures in every day for a specific fementer. It also plots ambient temperature and humidity.

    Args:
        fermenter (int): The fermenter to plot. Only positive integers allowed
        global_df (pandas.DataFrame): Dataframe with all required information
    """
    # Get averages of sensors
    average_df = global_df.groupby(level=0, axis=1).mean()
    # Create separate t-amb dataframe
    t_amb_df = pd.DataFrame(average_df['t_amb'])
    t_amb_df.insert(0, 'Día', t_amb_df.index.date)
    t_amb_df.insert(2, 'Medida', 'T-amb')
    t_amb_df.columns = t_amb_df.columns.str.replace('t_amb', 'Temperatura [$^oC$]')
    # Create separate fermenter dataframe
    fermenter_df = pd.DataFrame(average_df[f'f{fermenter}'])
    fermenter_df.insert(0, 'Día', average_df.index.date)
    fermenter_df.insert(2, 'Medida', f'Promedio Ferm. {fermenter}')
    fermenter_df.columns = fermenter_df.columns.str.replace(f'f{fermenter}', 'Temperatura [$^oC$]')
    # Create joint dataframe
    joint_df = pd.concat([fermenter_df, t_amb_df], ignore_index=True)
    
    plt.figure()
    sn.violinplot(data=joint_df, x='Día', y='Temperatura [$^oC$]', hue='Medida')
    plt.xticks(rotation=45)
    plt.xlabel('Día', fontsize='x-large')
    plt.ylabel('Temperatura [$^oC$]', fontsize='x-large')
    plt.title(f'Graficas de violin para fermentador {fermenter}', fontsize='xx-large')
    plt.tight_layout()
    plt.grid()
    plt.show()

def plot_3d_profile(fermenter, global_df):
    """
    This function plots a 3D interpolated profile of one fermenter in the last moment in global_df

    Args:
        fermenter (int): Fermenter to plot 3D profile
        global_df (pandas.DataFrame): Global dataframe with all necesary information to plot
    """
    input_temps = global_df[f'f{fermenter}'].iloc[-1, :].values

    # TODO: Handle correctly the dimensions of the fermenter
    # Define spacing in system
    coor_0 = [0,0,0]
    h = 13 # cm
    w = 7 # cm

    # Initialize array
    input_array = np.zeros((2, 2, 3))
    # Initialize observed temperatures
    obs_temps = np.zeros((4,4,3))

    # Asign inputs to array
    count = 0
    for i in range(input_array.shape[0]):
        for j in range(input_array.shape[1]):
            for k in range(input_array.shape[2]):
                input_array[i,j,k] = input_temps[count]
                count+=1

    # Make symmetric complete array
    first_flip = np.flip(input_array, axis = 0)
    second_flip = np.flip(input_array, axis = 1)
    third_flip =  np.flip(first_flip, axis = 1)

    # Assign to final obs_temps
    obs_temps[:2,:2,:] = input_array
    obs_temps[2:,:2,:] = first_flip
    obs_temps[:2,2:,:] = second_flip
    obs_temps[2:,2:,:] = third_flip

    # Flatten temps
    obs_temp_flat = obs_temps.reshape(-1,1)

    # Temperature parameters
    min_temp = 10.0
    max_temp = 60.0

    # Define padding parameter of the box sensors'
    min_padding = [5, 5, 5] # cm format x, y, z
    max_padding = [5, 5, 5] # cm format x, y, z

    # Define 1D vectors of observed coordinates
    x = np.arange(coor_0[0], 3*w+1, w)
    y = np.arange(coor_0[1], 3*w+1, w)
    z = np.arange(coor_0[2], 2*h+1, h)

    # Create flat coordinate vector of sampled points
    mesh_obs_coor =  np.meshgrid(x,y,z)
    obs_coor = [c.reshape(-1,1) for c in mesh_obs_coor]
    obs_coor_flat = np.hstack(obs_coor)

    # Set random temperature for test
    #obs_temps = 10 + np.random.rand(obs_coor_flat.shape[0], 1)*50

    # Obtain interpolator function
    interp_funct = interp.RBFInterpolator(obs_coor_flat, obs_temp_flat, kernel='linear')

    # Define 1D vectors of interpolated coordinates
    num_points = 20
    x_interp = np.linspace(coor_0[0] - min_padding[0], 3*w + max_padding[0], num_points)
    y_interp = np.linspace(coor_0[1] - min_padding[1], 3*w + max_padding[0], num_points)
    z_interp = np.linspace(coor_0[2] - min_padding[2], 2*h + max_padding[0], num_points)

    x_interp_c = np.linspace(coor_0[0] - min_padding[0], 3*w + max_padding[0], num_points+1)
    y_interp_c = np.linspace(coor_0[1] - min_padding[1], 3*w + max_padding[0], num_points+1)
    z_interp_c = np.linspace(coor_0[2] - min_padding[2], 2*h + max_padding[0], num_points+1)

    # Create flat coordinate vector of interpolated points
    mesh_interp_coor =  np.meshgrid(x_interp, y_interp, z_interp)
    interp_coor = [c.reshape(-1,1) for c in mesh_interp_coor]
    interp_coor_flat = np.hstack(interp_coor)

    # Get interpolated temperatures
    interp_t = interp_funct(interp_coor_flat)

    # Color function
    def cstm_plasma(x):
        return plt.cm.hot_r((np.clip(x,min_temp,max_temp)-min_temp)/(max_temp-min_temp))

    # Interpolated color values
    color_t = cstm_plasma(interp_t)[:,0,:]

    cube = np.ones(mesh_interp_coor[0].shape, dtype=bool)
    cube = cube[:-1,:-1,:-1]

    colors = np.reshape(color_t,  (num_points, num_points, num_points, 4))
    colors = colors[:-1, :-1, :-1]

    # Plot just shell
    cube[1:-1,1:-1,1:-1] = False 

    mesh_xy_interp =  np.meshgrid(x_interp, y_interp)
    interp_xy = [c.reshape(-1,1) for c in mesh_xy_interp]
    interp_xy_flat = np.hstack(interp_xy)

    # Get interpolated temperatures bottom
    interp_t_floors = [interp_funct(np.hstack((interp_xy_flat, level * np.ones((interp_xy_flat.shape[0], 1))))) for level in z]
    # Get interpolated colors
    interp_colors_floors = [cstm_plasma(temp)[:,0,:] for temp in interp_t_floors]
    colors_floors = [np.reshape(c_floors,  (num_points, num_points, 4)) for c_floors in interp_colors_floors]

    # Equate axis aspect ratio
    def axisEqual3D(ax):
        extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
        sz = extents[:,1] - extents[:,0]
        centers = np.mean(extents, axis=1)
        maxsize = max(abs(sz))
        r = maxsize/2
        for ctr, dim in zip(centers, 'xyz'):
            getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)

    def add_sampled_points(m_pad, x, y, ax):
        for i in range(2):
            for j in range(2):
                circle = plt.Circle((x[i]+m_pad[0]+0.5, y[j]+m_pad[1]+0.5), 
                                    0.7, 
                                    color='k', 
                                    fill = False)
                ax.add_patch(circle)

    extend_var = [np.min(x_interp)+min_padding[0], np.max(x_interp)+max_padding[0],
                np.min(y_interp)+min_padding[1], np.max(y_interp)+max_padding[1]]
        
    # Fontdict definicion
    font = {'family': 'serif',
            'weight': 'normal',
            'size': 16,
            }


    # Plot
    fig = plt.figure(constrained_layout=True, figsize=(10,8))
    gs = fig.add_gridspec(3, 3)
    ax = fig.add_subplot(gs[:,0:2], projection='3d')
    ax.voxels(mesh_interp_coor[0],
            mesh_interp_coor[1],
            mesh_interp_coor[2],
            cube,
            facecolors = colors,
            edgecolor= (0, 0, 0, 0.2))

    plt.title("3D Profile", fontsize=30, fontdict= font)
    axisEqual3D(ax)
    plt.axis('off')


    ax1 = fig.add_subplot(gs[0,2])
    plt.imshow(colors_floors[2], origin='lower',
            extent = extend_var)
    add_sampled_points(min_padding, x, y, ax1)
    plt.title(r'Top $z ='+str(min_padding[2]+z[0])+'$ cm', fontdict= font)
    plt.xlabel("$x~(cm)$", fontsize = 10, fontdict=font)
    plt.ylabel("$y~(cm)$", fontsize = 10, fontdict=font)

    ax2 = fig.add_subplot(gs[1,2])
    plt.imshow(colors_floors[1], origin='lower',
            extent = extend_var)
    add_sampled_points(min_padding, x, y, ax2)
    plt.title(r'Middle $z ='+str(min_padding[2]+z[1])+'$ cm', fontdict= font)
    plt.xlabel("$x~(cm)$", fontsize = 10, fontdict=font)
    plt.ylabel("$y~(cm)$", fontsize = 10, fontdict=font)

    ax3 = fig.add_subplot(gs[2,2])
    plt.imshow(colors_floors[0], origin='lower',
            extent = extend_var)
    add_sampled_points(min_padding, x, y,ax3)
    plt.title(r'Bottom $z ='+str(min_padding[2]+z[2])+'$ cm', fontdict= font)
    plt.xlabel("$x~(cm)$", fontsize = 10, fontdict=font)
    plt.ylabel("$y~(cm)$", fontsize = 10, fontdict=font)

    # Colorbar Code
    norm = matplotlib.colors.Normalize(vmin=min_temp, vmax=max_temp)
    m = cm.ScalarMappable(cmap=plt.cm.hot_r, norm=norm)
    m.set_array([])
    cbar = plt.colorbar(m, ax=[ax1, ax2, ax3], 
                        shrink=1, 
                        label=r'Temperature($^o$C)',
                        aspect= 35)
    cbar.ax.tick_params(labelsize=15)
    ax = cbar.ax
    text = ax.yaxis.label
    font = matplotlib.font_manager.FontProperties(family='serif', size=20)
    text.set_font_properties(font)

    plt.show()