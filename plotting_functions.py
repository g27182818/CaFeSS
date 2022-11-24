import matplotlib.pyplot as plt
from matplotlib import pylab
import seaborn as sn
import numpy as np
import pandas as pd
import gc
import os
import time
import datetime
import glob
import imageio
from matplotlib import cm
import scipy.interpolate as interp
import matplotlib
import matplotlib.patches as mpatches
from tqdm import trange
from utils import filter_global_df# , initialize_camera

matplotlib.use('agg')
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

def plot_fermenter_sensors(fermenter, global_df, resample=None, axis = None):
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
    if resample is not None:
        fermenter_df = global_df[f'f{fermenter}'].resample(resample, offset='0h0min1s').mean()
    else:
        fermenter_df = global_df[f'f{fermenter}']
    fermenter_df = fermenter_df.add_prefix('T Sensor ')
    fermenter_df.index.name, fermenter_df.columns.name = None, None

    # Get ambient temperature data
    if resample is not None:
        t_amb_df = global_df['t_amb'].resample(resample, offset='0h0min1s').mean()
    else:
        t_amb_df = global_df['t_amb']
    t_amb_df = t_amb_df.add_prefix('T-amb ')
    t_amb_df.index.name, t_amb_df.columns.name = None, None

    # Get ambient humidity data
    if resample is not None:
        h_amb_df = global_df['h_amb'].resample(resample, offset='0h0min1s').mean()
    else:
        h_amb_df = global_df['h_amb']
    h_amb_df = h_amb_df.add_prefix('H-amb ')
    h_amb_df.index.name, h_amb_df.columns.name = None, None

    # Handle xlim whe we have just some data points
    xlim_tup = (None, None) if fermenter_df.index.min() == fermenter_df.index.max() else (fermenter_df.index.min(), fermenter_df.index.max())

    # Plot Fermenters
    ax1 = fermenter_df.plot( xlim = xlim_tup, xlabel='Fecha-Hora', ax=axis)

    # Plot ambient temperatures
    t_amb_df.plot(ax=ax1, style='--', color=['k', 'gray'], grid=True, ylim = (0.0, 60.0))

    shade_day_night(global_df) 
    plt.ylabel('Temperatura [$^oC$]', fontsize='x-large')
    plt.xlabel('Fecha-Hora', fontsize='x-large')
    plt.title(f'Sensores de fermentador {fermenter} cada {resample}', fontsize='x-large')

    # Plot humidity data
    ax2 = plt.twinx()
    h_amb_df.plot(ylim = (0.0, 100.0),
                  ax=ax2, style='--', color=['b', 'c'])
    plt.ylabel('Humedad ambiente [%]', fontsize='x-large')
    ax2.spines['right'].set_color('b')
    ax2.tick_params(axis='y', colors='b')
    ax2.yaxis.label.set_color('b')
    
    # Add legends
    # Get day and night patches handles
    night_patch = mpatches.Patch(facecolor='grey', edgecolor='none', alpha=.3, label='Noche')
    day_patch = mpatches.Patch(facecolor='white', edgecolor='black', label='Día')
    handles = [day_patch, night_patch]
    # Get automatic legends from axis 1
    automatic_handles, labels = ax1.get_legend_handles_labels()
    # Put all handles together
    handles.extend(automatic_handles)
    ax1.legend(handles=handles, loc='center left',bbox_to_anchor=(1.15, 0.49))
    ax2.legend(loc='best')

    # Format figure
    plt.tight_layout()

# TODO: Be sure that this function can correctly plot all fermenters
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

    # Handle xlim whe we have just some data points
    xlim_tup = (None, None) if plot_df.index.min() == plot_df.index.max() else (plot_df.index.min(), plot_df.index.max())
    # Plot Fermenters
    plot_df.plot(grid=True, xlim = xlim_tup,
                 ax=ax1, style='o-', yerr=std_df, capsize=4, ylim = (0.0, 60.0))
    plt.xlabel('Fecha-Hora', fontsize='x-large')
    plt.ylabel('Temperatura [$^oC$]', fontsize='x-large')
    plt.title(title_str, fontsize='x-large')
    shade_day_night(global_df)

    # Plot humidity data
    ax2 = plt.twinx()
    h_amb_plot_df.plot(ylim = (0.0, 100.0),
                  ax=ax2, label='H-amb', style='--.b')
    plt.ylabel('Humedad ambiente [%]', fontsize='x-large')
    ax2.spines['right'].set_color('b')
    ax2.tick_params(axis='y', colors='b')
    ax2.yaxis.label.set_color('b')
    
    # Add legends
    # Get day and night patches handles
    night_patch = mpatches.Patch(facecolor='grey', edgecolor='none', alpha=.3, label='Noche')
    day_patch = mpatches.Patch(facecolor='white', edgecolor='black', label='Día')
    handles = [day_patch, night_patch]
    # Get automatic legends from axis 1 and 2
    automatic_handles1, _ = ax1.get_legend_handles_labels()
    automatic_handles2, _ = ax2.get_legend_handles_labels()
    # Join all legend handles
    handles.extend(automatic_handles2)
    handles.extend(automatic_handles1)
    # Set legends of the plot 
    ax1.legend(handles = handles, loc = 'best', title = 'Promedios', framealpha=1.0)

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
    # Modify labels to not show dates alwas
    mod_labels = [x.split()[1] if x.split()[1] != '0-6h' else x for x in labels]

    # Define color pallete for day and night
    palette = {x:('white' if (x.split('-')[-1]=='12h') or (x.split('-')[-1]=='18h') else 'gray') for x in labels}

    # Plot violin plot and ambient temperature
    sn.violinplot(data=fermenter_df, x='day_hour', y='Temperatura [$^oC$]', linewidth=0.7, palette=palette)
    plt.plot(np.arange(len(labels)), th_amb_df['t_amb'], 'o--k', markersize=3, label = 'T ambiente', alpha=0.7)
    # Format figure
    plt.xlim([-1, len(labels)])
    plt.ylim([0.0, 60.0])
    plt.grid()
    plt.xlabel('Día', fontsize='x-large')
    plt.ylabel('Temperatura [$^oC$]', fontsize='x-large')
    plt.xlabel('Fecha-Hora', fontsize='x-large')
    plt.title(f'Graficas de violín para fermentador {fermenter} cada 6 horas', fontsize='x-large')
    plt.xticks(ticks = np.arange(len(mod_labels)), labels=mod_labels, rotation=90)
    # Get axis 1
    ax1 = plt.gca()

    # Plot humidity data
    ax2 = plt.twinx()
    plt.plot(np.arange(len(labels)), th_amb_df['h_amb'], 'o--b', markersize=3, label = 'H ambiente', alpha=0.7)
    plt.ylabel('Humedad ambiente [%]', fontsize='x-large')
    plt.ylim([0.0, 100.0])
    ax2.spines['right'].set_color('b')
    ax2.tick_params(axis='y', colors='b')
    ax2.yaxis.label.set_color('b')

    # Add legends
    # Get day and night patches handles
    night_patch = mpatches.Patch(facecolor='grey', edgecolor='black', label='Noche')
    day_patch = mpatches.Patch(facecolor='white', edgecolor='black', label='Día')
    handles = [day_patch, night_patch]
    # Get automatic Handles
    automatic_handles1, _ = ax1.get_legend_handles_labels()
    automatic_handles2, _ = ax2.get_legend_handles_labels()
    # Join all Handles
    handles.extend(automatic_handles1)
    handles.extend(automatic_handles2)
    # Draw legend
    ax1.legend(handles=handles, loc='best', framealpha=1.0)

    plt.tight_layout()

def plot_fermenter_complete(fermenter, global_df, resample, path=None):
    """
    This function draws a figure with 3 plots:
    1. All the sensors from a fermenter resampled if desired
    2. The average temperature of the fermenter resampled if desired
    3. A violin plot of the fermenter every 6 hours. Can not be resampled.

    Args:
        fermenter (int): Fermenter to plot. Positive integer.
        global_df (pandas.DataFrame): Dataframe with all required information
        resample (str): String specifying the frequency to resample data. Cannot be less than the original sampling frequency.
        path (str): Optional parameter to specify where to store the plot. If none the plot is saved in os.path.join('data','current_ferm_state', f'f{fermenter}.jpeg')
    """
    fig = plt.figure(figsize=(14,10))

    # Plot all sensors from a fermenter resampled
    ax1 = plt.subplot(2,2,1)
    plot_fermenter_sensors(fermenter, global_df, resample = None, axis=ax1)

    # Plot the fermenter average temperature resampled
    plt.subplot(2,2,2)
    plot_fermenter_average(fermenter, global_df, resample = resample)

    # Plot violin plots not resampled
    plt.subplot(2,1,2)
    plot_fermenter_violin(fermenter, global_df)

    fig.suptitle(f'Comportamiento Fermentador {fermenter}', fontsize='xx-large')

    fig.tight_layout()

    # Creates dir to fermenter images if they do now exist
    os.makedirs(os.path.join('data','current_ferm_state'), exist_ok=True)

    # Save fermenter plot
    if path is not None:
        plt.savefig(path, dpi=500)
    else:    
        plt.savefig(os.path.join('data','current_ferm_state', f'f{fermenter}.jpeg'), dpi=500)
    plt.close()

def plot_3d_profile(fermenter, global_df, spanish=True):
    """
    This function plots a 3D interpolated profile of one fermenter in the last moment in global_df

    Args:
        fermenter (int): Fermenter to plot 3D profile
        global_df (pandas.DataFrame): Global dataframe with all necesary information to plot
    """
    input_temps = global_df[f'f{fermenter}'].iloc[-1, :].values
    time_string = global_df.index[-1].strftime("%Y-%m-%d %H:%M:%S")
    save_string = global_df.index[-1].strftime("%Y-%m-%d %H-%M-%S")+'.jpeg'

    # TODO: Handle correctly the dimensions of the fermenter
    # Define spacing in system
    coor_0 = [0,0,0]
    h = 13 # cm
    w = 7 # cm

    # Initialize array
    input_array = np.zeros((2, 2, 3))
    # Initialize observed temperatures
    obs_temps = np.zeros((4,4,3))

    # Assign inputs to array
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
    num_points = 15
    x_interp = np.linspace(coor_0[0] - min_padding[0], 3*w + max_padding[0], num_points)
    y_interp = np.linspace(coor_0[1] - min_padding[1], 3*w + max_padding[0], num_points)
    z_interp = np.linspace(coor_0[2] - min_padding[2], 2*h + max_padding[0], num_points)

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
    # ube[1:-1,1:-1,1:-1] = False # This plots all the outer shell
    cube[1:,:-1,:-1] = False # This plots just the outer shell visible to the user

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
                circle = plt.Circle((x[i]+m_pad[0]+0.5, y[j]+m_pad[1]+0.5), 0.7, color='k', fill = False)
                ax.add_patch(circle)

    extend_var = [np.min(x_interp)+min_padding[0], np.max(x_interp)+max_padding[0],
                np.min(y_interp)+min_padding[1], np.max(y_interp)+max_padding[1]]
        
    # Fontdict definicion
    font = {'family': 'serif',
            'weight': 'normal',
            'size': 16}
    
    plot_str_dict = {   'title': f"Perfil 3D fermentador {fermenter} en tiempo:\n{time_string}" if spanish else f"3D Profile of fermenter {fermenter} at time:\n{time_string}",
                        'top': f'Superior $z = {min_padding[2]+z[0]}$ cm' if spanish else f'Top $z ={min_padding[2]+z[0]}$ cm',
                        'middle': f'Medio $z = {min_padding[2]+z[1]}$ cm' if spanish else f'Middle $z ={min_padding[2]+z[1]}$ cm',
                        'bottom': f'Inferior $z = {min_padding[2]+z[2]}$ cm' if spanish else f'Bottom $z = {min_padding[2]+z[2]}$ cm',
                        'temperature': 'Temperatura($^o$C)' if spanish else 'Temperature($^o$C)'}


    # Plot
    fig = plt.figure(constrained_layout=True, figsize=(11,8))
    gs = fig.add_gridspec(3, 3)
    ax = fig.add_subplot(gs[:,0:2], projection='3d')
    ax.voxels(mesh_interp_coor[0],
            mesh_interp_coor[1],
            mesh_interp_coor[2],
            cube,
            facecolors = colors,
            edgecolor= (0, 0, 0, 0.2))

    plt.title(plot_str_dict['title'], fontsize=22, fontdict= font)
    axisEqual3D(ax)
    plt.axis('off')


    ax1 = fig.add_subplot(gs[0,2])
    plt.imshow(colors_floors[2], origin='lower',
            extent = extend_var)
    add_sampled_points(min_padding, x, y, ax1)
    plt.title(plot_str_dict['top'], fontdict= font)
    plt.xlabel("$x~(cm)$", fontsize = 10, fontdict=font)
    plt.ylabel("$y~(cm)$", fontsize = 10, fontdict=font)

    ax2 = fig.add_subplot(gs[1,2])
    plt.imshow(colors_floors[1], origin='lower',
            extent = extend_var)
    add_sampled_points(min_padding, x, y, ax2)
    plt.title(plot_str_dict['middle'], fontdict = font)
    plt.xlabel("$x~(cm)$", fontsize = 10, fontdict = font)
    plt.ylabel("$y~(cm)$", fontsize = 10, fontdict = font)

    ax3 = fig.add_subplot(gs[2,2])
    plt.imshow(colors_floors[0], origin='lower',
            extent = extend_var)
    add_sampled_points(min_padding, x, y,ax3)
    plt.title(plot_str_dict['bottom'], fontdict= font)
    plt.xlabel("$x~(cm)$", fontsize = 10, fontdict=font)
    plt.ylabel("$y~(cm)$", fontsize = 10, fontdict=font)

    # Colorbar Code
    norm = matplotlib.colors.Normalize(vmin=min_temp, vmax=max_temp)
    m = cm.ScalarMappable(cmap=plt.cm.hot_r, norm=norm)
    m.set_array([])
    cbar = plt.colorbar(m, ax=[ax1, ax2, ax3], 
                        shrink=1, 
                        label=plot_str_dict['temperature'],
                        aspect= 35)
    cbar.ax.tick_params(labelsize=15)
    ax = cbar.ax
    text = ax.yaxis.label
    font = matplotlib.font_manager.FontProperties(family='serif', size=20)
    text.set_font_properties(font)

    os.makedirs(os.path.join('data', 'current_3d_profiles'), exist_ok=True)
    os.makedirs(os.path.join('data', 'previous_3d_profiles', f'f{fermenter}'), exist_ok=True)
    fig.savefig(os.path.join('data', 'current_3d_profiles', f'f{fermenter}.jpeg'), dpi=300)
    fig.savefig(os.path.join('data', 'previous_3d_profiles', f'f{fermenter}', save_string), dpi=300)

    # This part frees up memory usage avoiding memory leak problems 
    # TODO: Implement this in all other plots
    plt.clf()
    plt.close('all')
    gc.collect()


def save_all_3d_plots(global_df):
    """
    This function receives a global information dataframe and uses plot_3d_profile() to save all images of a all the fermenters in all the datetimes

    Args:
        global_df (pandas.DataFrame): Multi-index dataframe with a cacao fermentation experiment data.
    """
    # Get the number of fermenters
    level_0 = global_df.columns.get_level_values(level=0).unique()
    n = len([x for x in level_0 if x[0]=='f'])
    
    # Cycle over dates
    for i in trange(global_df.shape[0]):
        line = global_df.iloc[[i], :]
        # Cycle over fermenters
        for j in range(n):
            plot_3d_profile(j+1, line)
            
def make_gif(fermenter, path = None):
    """
   This function receives a fermenter, loads all the heatmap images for that fermenter from data/heat_map_plots and saves a GIF
    of the time course of the fermenter.

    Args:
        fermenter (int): Number of the fermenter to make GIF.
        path (str): Path to save the GIF file. If None stores file in os.path.join('data', 'current_gifs', f'f{fermenter}.gif'). Defaults to None.

    Raises:
        ValueError: If no images are stored already for the given fermenter.
    """
    # Get image paths
    images_paths = sorted(glob.glob(os.path.join('data', 'previous_3d_profiles', f'f{fermenter}', '*.jpeg')))
    # Raise error
    if len(images_paths) == 0:
        raise ValueError(f'No images are already stored for fermenter {fermenter}')
    
    # If no path is specified store gif in current gifs folder
    if path is None:
         # Create gif directory
        os.makedirs(os.path.join('data', 'current_gifs'), exist_ok=True)
        # Assign store path
        path = os.path.join('data', 'current_gifs', f'f{fermenter}.gif')

    # Create GIF
    with imageio.get_writer(path, mode='I', duration=0.2) as writer:
        t = trange(len(images_paths))
        t.set_description(f'Generating GIF fermenter {fermenter}')
        for i in t:
            filename = images_paths[i]
            image = imageio.imread(filename)
            writer.append_data(image)

def request_plot(request_dict, global_df):
    """
    This function recieves a dictionary that specifies a required plot, makes the plot, saves it and returns a path where the plot is stored.

    Args:
        request_dict (dict):    This dictionary has all the necessary details to make the plot that the user wants. The keys are:
                                'start_date':   E.g. -1. String in the format of pysimplegui calendar button output to define start date of the plot.
                                                -1 to use the beginning of the global dataframe. If 'plot'=='3d_temp_gif' or 'thermal_camera' this
                                                argument will not be taken into acount. Note that if 'start_date'==-1 then also 'end_date'=-1.
                                'end_date':     E.g. -1. String or int in the format of pysimplegui calendar button output to define end date of the plot.
                                                -1 to use the end of the global dataframe. If 'plot'=='3d_temp_gif' or 'thermal_camera' this
                                                argument will not be taken into acount. Note that if 'end_date'==-1 then also 'start_date'=-1.
                                'fermenter':    E.g. -1. Int specifying the fermenter to plot. Must be -1 or bellow the total number of fermenters.
                                                Argument -1 will only work for 'plot'=='mean_std_fermenter' to show all fermenters. There is no fermenter 0.
                                                They start from 1.
                                'plot':         E.g.'complete_fermenter'. String specifying the plot to do. choices = ['complete_fermenter', 'violin_fermenter',
                                                'all_sensors_fermenter', 'mean_std_fermenter', '3d_temp', 'thermal_camera']
                                'resampling':   E.g. '1D'. String with possible resampling that can be used for 'plot'==['complete_fermenter', 'all_sensors_fermenter',
                                                'mean_std_fermenter']. choices = ['1h', '2h', '3h', '6h', '12h', '1D'].
        global_df (Pandas.DataFrame): Dataframe with all the needed data to make each plot.

    Returns:
        str: A string with the path to the stored plot.
    """
    # If start and end dates are not specified the don't perform any filtering of global_df
    if (request_dict['start_date'] == -1) and (request_dict['end_date'] == -1):
        filtered_df = global_df
    # Filter global_df with start and end if specified
    elif (request_dict['start_date'] != -1) and (request_dict['end_date'] != -1):
        filtered_df = filter_global_df(global_df, request_dict['start_date'], request_dict['start_date'])
    else:
        raise ValueError('Invalid date filtering for global dataframe. Start and end date must both be "-1" or neither of them should be "-1".')

    # Create folder of requested plots if it does not exists
    os.makedirs(os.path.join('data', 'requested_plots'), exist_ok=True)
    # Get the path from the now string for images that are not already generated
    path = os.path.join('data', 'requested_plots', f'{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}_{request_dict["plot"]}.jpeg')

    # Handle all the different kinds of plots
    if request_dict['plot']=='complete_fermenter':
        plot_fermenter_complete(request_dict['fermenter'], filtered_df, request_dict['resample'], path=path)

    elif request_dict['plot']== 'violin_fermenter':
        plt.figure(figsize=(14, 5))
        plot_fermenter_violin(request_dict['fermenter'], filtered_df)
        plt.savefig(path, dpi=300)
        plt.close()

    elif request_dict['plot']== 'all_sensors_fermenter':
        plt.figure(figsize=(7, 5))
        plot_fermenter_sensors(request_dict['fermenter'], filtered_df, request_dict['resample'])
        plt.savefig(path, dpi=300)
        plt.close()

    elif request_dict['plot']== 'mean_std_fermenter':
        plt.figure(figsize=(7,5))
        plot_fermenter_average(request_dict['fermenter'], filtered_df, request_dict['resample'])
        plt.savefig(path, dpi=300)
        plt.close()

    # If the user requested the 3D gif then point to the path where the gif is already stored
    elif request_dict['plot']== '3d_temp':
        path = os.path.join('data', 'current_3d_profiles', f'f{request_dict["fermenter"]}.jpeg')


    # TODO: Make thermal camara photo work even when camera is disconnected
    # elif request_dict['plot']== 'thermal_camera':  
    #     mlx = initialize_camera()
    #     plt.figure(figsize=(7, 5))
    #     take_thermal_picture(mlx)
    #     plt.savefig(path, dpi=300)
    #     plt.close()

    else:
        raise ValueError('Invalid type of plot. Must be one of ["complete_fermenter", "violin_fermenter", "all_sensors_fermenter", "mean_std_fermenter", "3d_temp_gif", "thermal_camera"]')

    return path




# # TODO: Make appropiate documentation of this function. Also program it in english
# # TODO: Be sure that this function works
# def take_thermal_picture(mlx):
#     frame = np.zeros((24*32,)) # Inicialización del tamaño de la imagen, en total 768 pts en un vector de 1xn
#     mlx.getFrame(frame) # Se actualiza el vector frame con los datos de la camara

#     mlx_shape = (24,32) # Tamaño real de la imagen mlx90640 shape en forma de matriz
#     data_array = np.fliplr(np.reshape(frame,mlx_shape)) # Actualización del frame en data_frame, ahora es una matriz con los datos de la imagen

#     ax=plt.subplot(111) # Se crea un subplot (Necesario para agregar textos, colorbar, ext.)
#     N = 26
#     mean = np.mean(frame) # Se obtiene temperatura media
#     textstr = "Mean temperature: " + str(mean) + "°C" # Se crea el texto que acompañará a la imagen  
#     props = dict(boxstyle="round", facecolor = "wheat", alpha = 0.5) # estilo de la caja de texto
#     t1 = ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize = 14, fontstyle =  "italic",verticalalignment = "top", bbox = props) # Se crea una caja de texto
#     cmap=plt.get_cmap('jet',26) # Estilo de la barra de color
#     therm1 = ax.imshow(data_array,interpolation='none', cmap=cmap,vmin=10,vmax=60) # Se coloca la imagen del data_array en la figura
#     cbar = plt.colorbar(therm1, ticks=np.linspace(10, 260, N), label = "Temperature [°C]") # Se establece la barra de color
#     # Ahora se definen el titulo y los ejes
#     plt.title(label="Thermal view",
#           position=(0.5, 0.9),
#           fontdict={'family': 'Dejavu Serif',
#                     'color' : 'black',
#                     'weight': 'bold',
#                     'size': 16})

#     plt.xlabel("x-coordinate", size = 12)
#     plt.ylabel("y-coordinate", size = 12)


# # Format definition of requested plots
# requested_plot = {  'start_date': '-1', # '-1' to use the beginning of the global dataframe. String in the format of pysimplegui calendar button output. If 'plot'=='3d_temp_gif' or 'thermal_camera' this argument will not be taken into acount 
#                     'end_date': '-1', # '-1' to use the end of the global dataframe. String in the format of pysimplegui calendar button output. If 'plot'=='3d_temp_giff' this argument will not be taken into acount.
#                     'fermenter': -1, # Int specifying the fermenter to plot. Must be between -1 and the total number of fermenters. argument -1 will only work for 'plot'=='mean_std_fermenter' to show all fermenters. There is no fermenter 0. They start from 1.
#                     'plot': 'complete_fermenter', # String with the plot to do. choices = ['complete_fermenter', 'violin_fermenter', 'all_sensors_fermenter', 'mean_std_fermenter', '3d_temp_gif', 'thermal_camera'].
#                     'resampling': '1D' # String with possible resampling that can be used for 'plot'=='complete_fermenter' or 'all_sensors_fermenter' or 'mean_std_fermenter'. choices = ['1h', '3h', '6h', '12h', '1D'] 
#                     }