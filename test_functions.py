import pandas as pd
import datetime
import numpy as np
import os
from scipy import interpolate
import matplotlib.pyplot as plt

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


def generate_test_df(fermenters = 8, sensors = 12, days = 14, freq = '30min', general_noise = 2, start_noise = 2):
    """
    This function generates a global test dataframe with simulated noisy data for a cacao fermentation experiment.

    Args:
        fermenters (int, optional): Numeber of fermenters in the dataframe. Defaults to 8.
        sensors (int, optional): Number of sensors in each fermenter. Defaults to 12.
        days (int, optional): number of simulation days to use. Defaults to 14.
        freq (str, optional): Sampling frequency to generate the data. Defaults to '30min'.
        general_noise (int, optional): Variance of the gaussian distribution to be added as a noise to all data. Defaults to 2.
        start_noise (int, optional): Variance of the gaussian distribution added as an offset for all data. Defaults to 2.

    Returns:
        Pandas.Dataframe: Multiindex dataframe containing all the simulated data. Disclaimer: This data is not realistic. It is just
        to tune the plotting functions.
    """
    
    # Get start and end of the sampling process
    start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    end = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")

    # Make column names lists
    fermenter_list = [f'f{i+1}' for i in range(fermenters)]
    sensor_list = [f'{i+1}' for i in range(sensors)]
    # Make multiindex fermenter column names
    fermenter_columns = pd.MultiIndex.from_product([fermenter_list, sensor_list])
    # Make ambient meassures multiindex columns
    amb_columns = pd.MultiIndex.from_product([['t_amb', 'h_amb'], ['1', '2']])
    # Join fermenter and ambient columns
    test_columns = amb_columns.append(fermenter_columns)
    # Make datetime index for dataframe
    test_index = pd.date_range(start=start, end = end, freq=freq)

    # Generate test data
    # Fermenters
    t = np.linspace(0, 5, len(test_index)) # Time vector
    fermenter_temps = (20 + 30*(1-np.exp(-t))).reshape((-1,1)) # Simulated exponential curve
    fermenter_matrix = fermenter_temps + np.random.randn(1, fermenters*sensors)*start_noise # Add some start noise

    # Ambient meassures
    t_amb_matrix = fermenter_temps + np.random.randn(1, 2)*start_noise # Simulate ambient temperatures
    h_amb_matrix = (50 + 30*(1-np.exp(-t))).reshape((-1,1)) + np.random.randn(1, 2)*start_noise # Simulate hambient humidity

    # Join test data in single matrix test_data
    matrices = [t_amb_matrix, h_amb_matrix, fermenter_matrix]
    matrices = [mat + np.random.randn(mat.shape[0], mat.shape[1])*general_noise for mat in matrices] # Add gaussian noise to all dataset
    test_data = np.concatenate(tuple(matrices), axis=1)

    # Construct test_df with the data
    test_df = pd.DataFrame(test_data, index=test_index, columns=test_columns)
    # Set names correctly
    test_df.columns.names = [None, 'datetime']

    return test_df


def get_interpolated_real_data(resample_min=30):
    """
    This funtion reads the resources/real_data.csv file, interpolates it and returns a pandas dataframe with all the data
    and a datetime index.

    Args:
        resample_min (int, optional): This is the number of minutes between each interpolated point. Defaults to 30.

    Returns:
        pd.DataFrame: Complete dataframe with all interpolated data and datetime index.
    """

    start = datetime.datetime.today().replace(hour=8, minute=0) 

    # Read the raw data
    real_raw_data = pd.read_csv(os.path.join('resources', 'real_data.csv'), header=1)

    # Split raw data in fermenenter temps, ambient temps and humidity
    real_t_ferm = real_raw_data[['X', 'Y']].dropna().sort_values('X')
    real_t_amb = real_raw_data[['X.1', 'Y.1']].dropna().sort_values('X.1')
    real_h_amb = real_raw_data[['X.2', 'Y.2']].dropna().sort_values('X.2')

    # Get minimum total sampled time
    min_tot_time = min([real_t_ferm.iloc[-1,0], real_t_amb.iloc[-1,0], real_h_amb.iloc[-1,0]])
    # Subsaple data to have all shared maximum times
    real_t_ferm = real_t_ferm.loc[real_t_ferm['X'] <= min_tot_time, :]
    real_t_amb = real_t_amb.loc[real_t_amb['X.1'] <= min_tot_time, :]
    real_h_amb = real_h_amb.loc[real_h_amb['X.2'] <= min_tot_time, :]

    # Get the time between each final meassure in days
    day_interval = datetime.timedelta(minutes=resample_min)/datetime.timedelta(days=1)
    # Define interpolation time vector
    t_interpolate = np.arange(0, min_tot_time, day_interval)

    # Define final interpolated dataframe
    interpolated_df = pd.DataFrame({'t': t_interpolate})

    # Interpolate measures and add them to the interpolated dataframe
    interpolated_df['t_ferm'] = interpolate.interp1d(real_t_ferm['X'], real_t_ferm['Y'], fill_value="extrapolate")(t_interpolate)
    interpolated_df['t_amb'] = interpolate.interp1d(real_t_amb['X.1'], real_t_amb['Y.1'], fill_value="extrapolate")(t_interpolate)
    interpolated_df['h_amb'] = interpolate.interp1d(real_h_amb['X.2'], real_h_amb['Y.2'], fill_value="extrapolate")(t_interpolate)
    
    # Define datetime index
    interpolated_df.index = [(start + datetime.timedelta(days=d)).strftime("%Y-%m-%d %H:%M:%S") for d in interpolated_df['t']]
    # Drop day time
    interpolated_df.drop('t', axis='columns', inplace=True)

    return interpolated_df


def generate_realistic_test_df(fermenters = 8, sensors = 12, general_noise = 2, start_noise = 2):
    """
    This function generates a global test dataframe with simulated noisy data for a cacao fermentation experiment. The base to simulate
    the data is from the resources/real_data.csv file. Hence, this simulation is much more realistic than generate_test_df() function.
    However this function will only produce dataframes from 8 days.

    Args:
        fermenters (int, optional): Numeber of fermenters in the dataframe. Defaults to 8.
        sensors (int, optional): Number of sensors in each fermenter. Defaults to 12.
        general_noise (int, optional): Variance of the gaussian distribution to be added as a noise to all data. Defaults to 2.
        start_noise (int, optional): Variance of the gaussian distribution added as an offset for all data. Defaults to 2.

    Returns:
        Pandas.Dataframe: Multiindex dataframe containing all the simulated data. This data is realistic but it is just used
        to tune the plotting functions. It does not correspond to a real experiment.
    """
    # Get realistic interpolated data
    interpolated_df = get_interpolated_real_data()

    # Make column names lists
    fermenter_list = [f'f{i+1}' for i in range(fermenters)]
    sensor_list = [f'{i+1}' for i in range(sensors)]
    # Make multiindex fermenter column names
    fermenter_columns = pd.MultiIndex.from_product([fermenter_list, sensor_list])
    # Make ambient meassures multiindex columns
    amb_columns = pd.MultiIndex.from_product([['t_amb', 'h_amb'], ['1', '2']])
    # Join fermenter and ambient columns
    test_columns = amb_columns.append(fermenter_columns)
    # Make datetime index for dataframe
    test_index = pd.DatetimeIndex(interpolated_df.index)

    # Generate test data
    fermenter_matrix = interpolated_df['t_ferm'].values.reshape((-1, 1)) + np.random.randn(1, fermenters*sensors)*start_noise # Add some start noise
    t_amb_matrix = interpolated_df['t_amb'].values.reshape((-1, 1)) + np.random.randn(1, 2)*start_noise # Simulate ambient temperatures
    h_amb_matrix = interpolated_df['h_amb'].values.reshape((-1,1)) + np.random.randn(1, 2)*start_noise # Simulate hambient humidity
    
    # Join test data in single matrix test_data
    matrices = [t_amb_matrix, h_amb_matrix, fermenter_matrix]
    matrices = [mat + np.random.randn(mat.shape[0], mat.shape[1])*general_noise for mat in matrices] # Add gaussian noise to all dataset
    test_data = np.concatenate(tuple(matrices), axis=1)

    # Construct test_df with the data
    test_df = pd.DataFrame(test_data, index=test_index, columns=test_columns)
    # Set names correctly
    test_df.columns.names = [None, 'datetime']
    
    return test_df

