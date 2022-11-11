#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
from plotting_functions import *
from test_functions import *
from utils import *
from report_gen import make_report



##############################################################################
####################### Test code ############################################
##############################################################################

# # Number of fermenters
# fermenters = 8
# # Global dataframe to save all data
# global_df = pd.DataFrame()

# plot_fermenter(2, global_df)

# # Test cycle on 100 measures
# for i in range(10):
#     test_measure = generate_test_line(fermenters)
#     global_df = lecturadatos(global_df, test_measure)
#     time.sleep(1)


test_df = generate_realistic_test_df(fermenters = 8, sensors = 12, general_noise = 2, start_noise = 2)

# plot_fermenter_sensors(2, test_df, '10min')
# plot_fermenter_average(6, test_df, '1D')
# plot_fermenter_violin(6, test_df, day_night=True)
# plot_fermenter_complete(6, test_df, freq='30min', resample= '1D')
# start = time.time()
# plot_3d_profile(8, test_df)
# end = time.time()
# print(f'It takes {round(end-start, 2)}s to save a heatmap from one fermenter')
make_report(test_df, resample='1D')
# save_all_3d_plots(test_df)
# make_gif(fermenter=1)

# Test global_df filtering
# test_start = (datetime.datetime.today() + datetime.timedelta(days=2)).replace(hour=8, minute=0).strftime("%Y-%m-%d %H:%M:%S")
# test_end = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S") 
# test_filtered_df = filter_global_df(test_df, test_start, test_end)

##############################################################################
####################### End of Test code #####################################
##############################################################################


# Boton para camara terminca en tiempo real
