from turtle import color
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import pandas as pd
import os
import datetime
from matplotlib import cm
import scipy.interpolate as interp
import matplotlib
pd.options.mode.chained_assignment = None


def shade_day_night(global_df):
    """
    This function shadows day and night regions in temporal plots.

    Args:
        global_df (pandas.DataFrame): DataFrame containing the datetime index needed to plot data.
    """
    # Get the start and end day of medition
    start_day = global_df.index.min().date()
    end_day = global_df.index.max().date()

    # Define shadow edges
    shadow_start = datetime.datetime.combine(start_day +datetime.timedelta(days=-1) , datetime.time(18,0))
    shadow_end = end_day+datetime.timedelta(days=2)
    shadow_edges = pd.date_range(start=shadow_start, end=shadow_end, freq='12H')

    # Get current figure axis
    ax = plt.gca()

    # Plot shadows in current figure
    for i in range(len(shadow_edges)-2):
        if i%2==0:
            ax.axvspan(shadow_edges[i], shadow_edges[i+1], facecolor='gray', edgecolor='none', alpha=.3)

def plot_fermenter_sensors(fermenter, global_df, resample, axis = None):
    """
    This function plots all the sensors of a given fermenter resampled by time. It also plots ambient temperature and humidity.

    Args:
        fermenter (int): The fermenter to plot. Only positive integers.
        global_df (pandas.DataFrame): Dataframe with all required information
        resample (str): String specifying the frequency to resample data. Cannot be less than the original sampling frequency.
        axis (matplotlib.axis) : Axis object where to make the plot
    """
    # Get specific fermenter data
    # The offset is made to guarantee that the plot units are in seconds which make possible to draw day/night shading
    fermenter_df = global_df[f'f{fermenter}'].resample(resample, offset='0h0min1s').mean()
    fermenter_df = fermenter_df.add_prefix('Sensor ')
    fermenter_df.index.name, fermenter_df.columns.name = None, None
    # Get ambient temperature data
    t_amb_df = global_df['t_amb'].resample(resample, offset='0h0min1s').mean()
    t_amb_df = t_amb_df.add_prefix('T-amb ')
    t_amb_df.index.name, t_amb_df.columns.name = None, None

    # Get ambient humidity data
    h_amb_df = global_df['h_amb'].resample(resample, offset='0h0min1s').mean()
    h_amb_df = h_amb_df.add_prefix('H-amb ')
    h_amb_df.index.name, h_amb_df.columns.name = None, None

    # Plot Fermenters
    ax1 = fermenter_df.plot( xlim = (fermenter_df.index.min(), fermenter_df.index.max()), xlabel='Fecha-Hora', ax=axis)

    # Plot ambient temperatures
    t_amb_df.plot(ax=ax1, style='--', color=['k', 'gray'], grid=True,)

    shade_day_night(global_df) 
    plt.ylabel('Temperatura [$^oC$]', fontsize='x-large')
    plt.xlabel('Fecha-Hora', fontsize='x-large')
    plt.title(f'Sensores de fermentador {fermenter} cada {resample}', fontsize='x-large')

    # Plot humidity data
    ax2 = plt.twinx()
    h_amb_df.plot(ylim = (10.0, 100.0),
                  ax=ax2, style='--', color=['b', 'c'])
    plt.ylabel('Humedad ambiente [%]', fontsize='x-large')
    ax2.spines['right'].set_color('b')
    ax2.tick_params(axis='y', colors='b')
    ax2.yaxis.label.set_color('b')
    
    # Add legends
    ax1.legend(loc='center left',bbox_to_anchor=(1.15, 0.4))
    ax2.legend(loc='best')

    # Format figure
    plt.tight_layout()


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
    # The offset is made to guarantee that the plot units are in seconds which make possible to draw day/night shading
    t_amb_plot_df = average_df['t_amb'].resample(resample, offset='0h0min1s').mean()
    h_amb_plot_df = average_df['h_amb'].resample(resample, offset='0h0min1s').mean()
    
    # Handle to plot all fermenters or just one
    if fermenter == -1:
        # Case to plot all fermenters
        plot_df = average_df.iloc[:,average_df.columns.str.contains('f')].resample(resample).mean()
        std_df = None # Does not plot error bars when ploting all fermenters
        plot_df.columns = plot_df.columns.str.replace('f', 'Ferm. ') # Set names for plot labels
        title_str = 'Promedio de todos los fermentadores cada '+resample
    else:
        # Case to plot just one fermenter
        plot_df = average_df[f'f{fermenter}'].resample(resample, offset='0h0min1s').mean()
        # Compute standard deviation error bars
        std_df = average_df[f'f{fermenter}'].resample(resample, offset='0h0min1s').std()
        plot_df.name = f'Ferm. {fermenter}'
        title_str = f'Promedio de fermentador {fermenter} cada '+ resample

    # Plot ambient temperatures
    ax1 = t_amb_plot_df.plot(label='T-amb', style='--.k')

    # Plot Fermenters
    plot_df.plot(grid=True,
                xlim = (plot_df.index.min(), plot_df.index.max()),
                        ax=ax1, style='o-', yerr=std_df, capsize=4)
    plt.xlabel('Fecha-Hora', fontsize='x-large')
    plt.ylabel('Temperatura [$^oC$]', fontsize='x-large')
    plt.title(title_str, fontsize='x-large')
    shade_day_night(global_df)

    # Plot humidity data
    ax2 = plt.twinx()
    h_amb_plot_df.plot(ylim = (10.0, 100.0),
                  ax=ax2, label='H-amb', style='--.b')
    plt.ylabel('Humedad ambiente [%]', fontsize='x-large')
    ax2.spines['right'].set_color('b')
    ax2.tick_params(axis='y', colors='b')
    ax2.yaxis.label.set_color('b')
    
    # Set legends of 
    ax1.legend(loc='best')

    # Format figure
    plt.tight_layout()


def plot_fermenter_violin(fermenter, global_df):
    """
    This function plots boxplots for the measures in every day for a specific fementer. It also plots ambient temperature and humidity.

    Args:
        fermenter (int): The fermenter to plot. Only positive integers allowed
        global_df (pandas.DataFrame): Dataframe with all required information
    """
    # Get averages of sensors
    average_df = global_df.groupby(level=0, axis=1).mean()

    # Declre day/night vector
    hour_vec = ['0-6h', '6-12h', '12-18h', '18-24h']
    # Declare day/night funciton
    hour_fn = lambda x: hour_vec[int(x.time().strftime('%H')) // 6]

    # Create separate t-amb dataframe
    th_amb_df = average_df[['t_amb', 'h_amb']]
    th_amb_df.insert(0, 'Día', th_amb_df.index.date)
    th_amb_df.insert(2, 'Hora', th_amb_df.index.map(hour_fn))
    th_amb_df['day_hour'] = th_amb_df['Día'].map(lambda x: x.strftime("%Y-%m-%d")) + ' ' + th_amb_df['Hora']
    th_amb_df = th_amb_df.groupby('day_hour', sort=False).mean()
 
    # Create separate fermenter dataframe
    fermenter_df = pd.DataFrame(average_df[f'f{fermenter}'])
    fermenter_df.insert(0, 'Día', average_df.index.date)
    fermenter_df.insert(2, 'Medida', f'Promedio Ferm. {fermenter}')
    fermenter_df.insert(3, 'Hora', fermenter_df.index.map(hour_fn))
    fermenter_df['day_hour'] = fermenter_df['Día'].map(lambda x: x.strftime("%Y-%m-%d")) + ' ' + fermenter_df['Hora']
    fermenter_df.columns = fermenter_df.columns.str.replace(f'f{fermenter}', 'Temperatura [$^oC$]')

    # Get the labels for violin plot
    labels = list(fermenter_df['day_hour'].unique())
    labels = [x.split()[1] if x.split()[1] != '0-6h' else x for x in labels]
    
    # Plot violin plot and ambient temperature
    sn.violinplot(data=fermenter_df, x='day_hour', y='Temperatura [$^oC$]', color='r', linewidth=0.7)
    plt.plot(np.arange(len(labels)), th_amb_df['t_amb'], 'o--k', markersize=3, label = 'T ambiente', alpha=0.7)
    # Format figure
    plt.xlim([-1, len(labels)])
    plt.grid()
    plt.xlabel('Día', fontsize='x-large')
    plt.ylabel('Temperatura ambiente[$^oC$]', fontsize='x-large')
    plt.xlabel('Fecha-Hora', fontsize='x-large')
    plt.title(f'Graficas de violín para fermentador {fermenter} cada 6 horas', fontsize='x-large')
    plt.xticks(ticks = np.arange(len(labels)), labels=labels, rotation=90)

    # Plot humidity data
    ax2 = plt.twinx()
    plt.plot(np.arange(len(labels)), th_amb_df['h_amb'], 'o--b', markersize=3, label = 'H ambiente', alpha=0.7)
    plt.ylabel('Humedad ambiente [%]', fontsize='x-large')
    ax2.spines['right'].set_color('b')
    ax2.tick_params(axis='y', colors='b')
    ax2.yaxis.label.set_color('b')

    plt.tight_layout()


def plot_fermenter_complete(fermenter, global_df, freq, resample):
    """
    This function draws a figure with 3 plots:
    1. All the sensors from a fermenter resampled if desired
    2. The average temperature of the fermenter resampled if desired
    3. A violin plot of the fermenter every 6 hours. Can not be resampled.

    Args:
        fermenter (int): Fermenter to plot. Positive integer.
        global_df (pandas.DataFrame): Dataframe with all required information
        freq (str): String specifying the sample frequency of the data
        resample (str): String specifying the frequency to resample data. Cannot be less than the original sampling frequency.
    """
    fig = plt.figure(figsize=(14,10))

    # Plot all sensors from a fermenter resampled
    ax1 = plt.subplot(2,2,1)
    plot_fermenter_sensors(fermenter, global_df, resample= freq, axis=ax1)

    # Plot the fermenter average temperature resampled
    plt.subplot(2,2,2)
    plot_fermenter_average(fermenter, global_df, resample)

    # Plot violin plots not resampled
    plt.subplot(2,1,2)
    plot_fermenter_violin(fermenter, global_df)

    fig.suptitle(f'Comportamiento Fermentador {fermenter}', fontsize='xx-large')

    fig.tight_layout()

    # Creates dir to fermenter images if they do now exist
    if not os.path.exists(os.path.join('data','ferm_current_state')):
        os.makedirs(os.path.join('data','ferm_current_state'))

    # Save fermenter plot
    plt.savefig(os.path.join('data','ferm_current_state', f'f{fermenter}.png'), dpi=100)
    plt.close()



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