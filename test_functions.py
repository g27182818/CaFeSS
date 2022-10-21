import pandas as pd
import datetime
import numpy as np


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

