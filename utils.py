import datetime
import pandas as pd
import os
from plotting_functions import *
import serial
from PIL import Image
# import board,busio
# import adafruit_mlx90640

def initialize_arduino(serial_path = '/dev/ttyUSB0', serial_speed = 9600, test=True):
    # Test code. uncomment the next line to get real function
    if test:
        arduino = serial.Serial()
    else:
        arduino = serial.Serial(serial_path, serial_speed)
    return arduino

# This function gets string lines from the arduino
def read_arduino_line(arduino):
    # Read and decode lines from arduino
    arduino_line = arduino.readline()
    decoded_arduino_line = arduino_line.decode(encoding = 'utf-8')
    return decoded_arduino_line

# This function receives an arduino line and returns a pandas dataframe 
def get_pd_from_line(line, time_stamp=None):
    """
    This function receives a string line in arduino format and converts it into a one row multi-index dataframe to concat with global_df.
    It optionally receives a time_stamp that is used in testing the system to specify the time index in the resulting dataframe.

    Args:
        line (str): String line in arduino format.
        time_stamp (pandas._libs.tslibs.timestamps.Timestamp, optional): Optional time stamp to set the time index of the one row output dataframe. Defaults to None.

    Returns:
        pandas.DataFrame: One row pandas dataframe representing the data from the arduino line and with the global_df format.
    """
    # Get line without new lines
    line = line.split('\r')[0][:-1]
    print(line)
    # Split line by fermenter
    splitted_line = line.split('f')[1:] # splitted line for fermenter
    # Number of fermenters
    num_fer = len(splitted_line)

    # List of ambient temperature and humidity
    amb_list = line.split('f')[0].split(',')[:-1]

    # Define global dict to store current temperatures
    global_dict = { 't_amb-1': float(amb_list[1]),
                    't_amb-2': float(amb_list[2]),
                    'h_amb-1': float(amb_list[4]),
                    'h_amb-2': float(amb_list[5])}

    # Cycle in each fermenter to compute important things
    for i in range(num_fer):
        # Split each fermenter by comas and don't use the initial number. The if is to handle the last comma
        fermenter_list = splitted_line[i].split(',')[1:-1] if i != num_fer-1 else splitted_line[i].split(',')[1:]
        fermenter_list = [float(temp) for temp in fermenter_list]
        # Restart fermenter dict just in case
        fermenter_dict = {}
        # Declare fermenter dict
        fermenter_dict = {f'f{i+1}-{j+1}': [fermenter_list[j]] for j in range(len(fermenter_list))}
        # Append current information to global_dict
        global_dict = {**global_dict, **fermenter_dict}

    # Get pandas dataframe for current measurement
    output_df = pd.DataFrame.from_dict(global_dict)
    
    # Put date and time as index of current time if not specified
    if time_stamp is None:
        output_df.index = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        output_df.index = pd.to_datetime(output_df.index)
    
    # Or put date-time index specified by parameter
    else:
        output_df.index = pd.to_datetime([time_stamp])

    # Put multi-index in data
    output_df.columns = pd.MultiIndex.from_tuples([(c.split('-')[0], c.split('-')[1]) for c in output_df.columns])
    
    # Set names 
    output_df.columns.names = [None, 'datetime']

    # Return output dataframe
    return output_df

# This function receives arduino lines and updates the global dataframe of variables, saves updated files, and computes important statistics
def update_global_df(line, global_df = None, time_stamp=None):
    """
    This function receives the global dataframe, arduino lines and an optional time stamp for system test purposes.
    With that information the function updates the global dataframe of variables, saves updated files, and computes important statistics.

    Args:
        global_df (pandas.DataFrame): Global dataframe with all the data of the fermentation experiment.
        line (str): String line in arduino format.
        time_stamp (pandas._libs.tslibs.timestamps.Timestamp, optional): Optional time stamp to set the time index of the one row current dataframe
                                                                            that will be concatenated with global_df. Defaults to None.

    Raises:
        ValueError: If global dataframe has no data.

    Returns:
        global_df (pandas.DataFrame): An updated dataframe with the new arduino line at the end.
    """
    # Test code, comment in real application
    current_df = get_pd_from_line(line, time_stamp=time_stamp)
    
    # Concat normal dataframe with current measures. If global_df has nothing declare it as current_df
    global_df = current_df if global_df is None else pd.concat([global_df, current_df])

    # Get per day averages
    per_day_df = round(global_df.resample('D').mean(), 2)
    per_day_df.columns.names = [None, 'datetime']
    # Promedio de todos los sensores por fermentador
    per_fermenter_df = round(global_df.groupby(level=0, axis=1).mean(), 2)
    per_fermenter_df.index.name = 'datetime'

    # Ruta destino para guardar datos en csv
    os.makedirs(os.path.join('data'), exist_ok=True)

    # If this is the first datum then save with headers
    if global_df.shape[0] == 1:
        global_df.to_csv(os.path.join('data', 'global_df.csv'))
        per_fermenter_df.to_csv(os.path.join('data', 'per_fermenter_df.csv'))
    # For the next data just append to the csvs
    elif global_df.shape[0] > 1:
        global_df.iloc[[-1], :].to_csv(os.path.join('data', 'global_df.csv'), mode='a', header=None)
        per_fermenter_df.iloc[[-1], :].to_csv(os.path.join('data', 'per_fermenter_df.csv'), mode='a', header=None)
    else:
        raise ValueError('Global data frame has no data.')
    # Overwrite each time per day dataframe
    per_day_df.to_csv(os.path.join('data', 'per_day_df.csv'))

    return global_df

# This function filters a global dataframe with a start and end strings
def filter_global_df(global_df, start_str, end_str):
    start_datetime = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
    return global_df[start_datetime:end_datetime]

def is_it_measure_time(start, period, prev_cycle):
    elapsed_time = round((time.time() - start)/60, 2)
    cycles_passed = elapsed_time//period
    measure_bool = cycles_passed != prev_cycle
    prev_cycle = cycles_passed

    return elapsed_time, prev_cycle, measure_bool

def is_it_read_time(elapsed_time, period, read_wait):
    difference = round(elapsed_time%period, 2) - read_wait
    if (-1.5 < difference*60) and (difference*60 < 1.5):
        return True
    else:
        return False

def modify_image(path, width):
    image1 = Image.open(path)
    width_percent1 = (width / float(image1.size[0]))
    height_size1 = int((float(image1.size[1]) * float(width_percent1)))
    image1 = image1.resize((width, height_size1))
    new_path = path.replace('jpeg','png')
    image1.save(new_path)
    return new_path

# # This function initializes the thermal camera and returns a camera object
# def initialize_camera():
#     i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
#     mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
#     mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate
#     return mlx