'''
Title: VTP Functions

Description: Script used to process vehicle telematics data for associated
research paper.

Script Author: Alexander Yoshizumi
Paper Authors: Beia Spiller, Elizabeth Stein, Eleftheria Kontou,
Ruolin Zhang, Alexander Yoshizumi

Last Updated: 14 January 2024
'''
import sys
import datetime
import pandas as pd
import numpy as np
import statistics as st
import sys
import os
import glob

sys.path.insert(1, 'C:\\Users\\alexa\\OneDrive\\Documents\\GitHub\\VTP\\core')

import vtp_functions as vtp

# PROCESSING # 

# #cngsocal
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\cngsocal.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '.csv')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','cngsocal_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','cngsocal_cluster_input.csv'))


# #airportelectrification - remoteparking
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\airportelectrification.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','airportelectrification_remoteparking_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','airportelectrification_remoteparking_cluster_input.csv'))

# #airportelectrification - rentalcarshuttle
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\airportelectrification.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOOOOOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','airportelectrification_rentalcarshuttle_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','airportelectrification_rentalcarshuttle_cluster_input.csv'))

# #airportelectrification - employeeshuttle
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\airportelectrification.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOOOOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','airportelectrification_employeeshuttle_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','airportelectrification_employeeshuttle_cluster_input.csv'))

# #delivboxtrucksandiegoca
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\delivboxtrucksandiegoca.00',
#                                       file_level = 3,
#                                       var_format = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOO++++++++++++++++++++++++++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','delivboxtrucksandiegoca_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','delivboxtrucksandiegoca_cluster_input.csv'))

# #ornltransit
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\ornltransit.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVV+EEE+WW+OOOOOOO+++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','ornltransit_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','ornltransit_cluster_input.csv'))

# #parceldeliverytexas - regionalhaul
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\parceldeliverytexas.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parceldeliverytexas_regionalhaul_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parceldeliverytexas_regionalhaul_cluster_input.csv'))

# #parceldeliverytexas - parceldelivery
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\parceldeliverytexas.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOOOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parceldeliverytexas_parceldelivery_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parceldeliverytexas_parceldelivery_cluster_input.csv'))

# #parcelhyconminneapolis - ice
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\parcelhyconminneapolis.00',
#                                       file_level = 3,
#                                       var_format = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVV+EEE+W+OOOOOOOOOOOOOO+++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis_ice_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis_ice_cluster_input.csv'))

# #parcelhyconminneapolis - parhev
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\parcelhyconminneapolis.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVV+EEEEEE+W+OOOOOOOOOOOOOO+++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis_parhev_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis_parhev_cluster_input.csv'))

# #regionalhaulcolorado
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\regionalhaulcolorado.00',
#                                       file_level = 3,
#                                       var_format = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+W+OOOOOOOOO++++++++++++++++++++++++++++++++++++++++++++++++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','regionalhaulcolorado_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','regionalhaulcolorado_cluster_input.csv'))

# #regionalhaulohio
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\regionalhaulohio.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','regionalhaulohio_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','regionalhaulohio_cluster_input.csv'))

# #regionalhaultexas
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\regionalhaultexas.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOO+YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','regionalhaultexas_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','regionalhaultexas_cluster_input.csv'))

# #schoolbussocal
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\schoolbussocal.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOOO+++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','schoolbussocal_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','schoolbussocal_cluster_input.csv'))

# #parcelhyconminneapolis2 - ice
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\parcelhyconminneapolis2.00',
#                                       file_level = 3,
#                                       var_format = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVV+EEE+W+OOOOOOOOOOOOOO+++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis2_ice_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis2_ice_cluster_input.csv'))

# #parcelhyconminneapolis2 - parhev
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\parcelhyconminneapolis2.00',
#                                       file_level = 3,
#                                       var_format = '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVV+EEEEEE+W+OOOOOOOOOOOOOO+++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '')

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis2_parhev_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','parcelhyconminneapolis2_parhev_cluster_input.csv'))

# hydraulichyrefusemiamidade
# x,y = process_telematics_from_directory(directory = 'G:\\My Drive\\02_EDF\\Data\\01_Source\\hydraulichyrefusemiamidade.00',
#                                       file_level = 3,
#                                       var_format = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++VVVVV+EEE+WW+OOOOOOOOOOOO+++++++++++YYYY+MM+DD.csv',
#                                       speed_col = 'GpsSpeed',
#                                       new_speed_col = 'Speed',
#                                       time_col = 'DateTime_Logger_UTC',
#                                       time_format = 'YYYY-MM-DD hh:mm:ss-__:__',
#                                       new_time_col = 'Time',
#                                       file_filter_term = '',
#                                       interval = (60*60))

# x.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','hydraulichyrefusemiamidade_vehicle_state.csv'))
# y.to_csv(os.path.join('G:','My Drive','EDF','Data','02_Processed','hydraulichyrefusemiamidade_cluster_input.csv'))

#------------------------------------------------------------------------------

# TEST AREA #

# # Replace this file name with whatever file path you use.
# df1 = pd.read_csv('G:\\My Drive\\02_EDF\\Data\\01_Source\\cngsocal.00\\cngsocal.00.2019.c1.t12181.ice.08.transit.csv\\2019.c1.t12181.ice.08.transit\\2019.c1.t12181.ice.08.transit.2016-02-22.csv')

# vtp.add_date_time(df1,'DateTime_Logger_UTC','YYYY-MM-DD hh:mm:ss-__:__','Date_Time')

# vtp.add_time(df1,'DateTime_Logger_UTC','YYYY-MM-DD hh:mm:ss-__:__','Time')

# df2 = vtp.standardize_by_time(df1, time_column='Time')

# df2['GpsSpeed'] = df2['GpsSpeed'].fillna(0)

# df3 = vtp.average_over_interval(df2, column = 'GpsSpeed', interval = (60*15))

# dff = vtp.assign_vehicle_state(df = df3, time_column='Time',speed_column='GpsSpeed',spd_thr=0.01,str_thr=1,end_thr=1)