"""
Title: VTP Functions

Description: Vehicle telematics processing functions for creating derivative
data products from telematics data.

Author: Alexander Yoshizumi
With Contributions from: Eleftheria Kontou and Ruolin Zhang

Last Updated: 11 February 2022

"""

import datetime
import pandas as pd
import numpy as np
import statistics as st
import sys
import os
import glob


def substring_position(string, substring):
    r = [i for i in range(len(string)) if string.startswith(substring, i)]
    return r

def parse_date(date, form):
    '''
    Description:
    A function that extracts the year, month, and day from a date string.

    Attributes:
        date: The string containing the date of interest.
        form: The format of the date text string where 'Y' corresponds to year,
        'M' corresponds to month, and 'D' corresponds to day.
        
    Returns:
        datetime.date object
    '''
    
    # Identify positions of date components from user-provided formatting.
    y_pos = substring_position(string = form, substring = 'Y')
    m_pos = substring_position(string = form, substring = 'M')
    d_pos = substring_position(string = form, substring = 'D')
    
    # Store date components.
    year = str()
    month = str()
    day = str()
    
    for i in y_pos:
        year = year + date[i]
    
    for j in m_pos:
        month = month + date[j]
    
    for k in d_pos:
        day = day + date[k]
    
    return datetime.date(year = int(year),
                         month = int(month),
                         day = int(day))
    
def parse_time(time, form):
    '''
    Description:
    A function that extracts the hour, minute, and sencond from a time string.

    Attributes:
        time: The string containing the time of interest.
        form: The format of the date text string where 'h' corresponds to hour,
        'm' corresponds to minute, and 's' corresponds to second.
        
    Returns:
        datetime.time object
    '''
    
    # Identify positions of date components from user-provided formatting.
    h_pos = substring_position(string = form, substring = 'h')
    m_pos = substring_position(string = form, substring = 'm')
    s_pos = substring_position(string = form, substring = 's')
    
    # Store date components.
    hour = str()
    minute = str()
    second = str()
    
    for i in h_pos:
        hour = hour + time[i]
    
    for j in m_pos:
        minute = minute + time[j]
    
    for k in s_pos:
        second = second + time[k]
    
    return datetime.time(hour = int(hour),
                         minute = int(minute),
                         second = int(second))

def parse_date_time(date_time, form):
    '''
    Description:
    A function that extracts the hour, minute, and sencond from a time string.
    
    Attributes:
        date: The string containing the date of interest.
        time: The string containing the time of interest.
        form: The format of the date text string where 'Y' corresponds to year,
        'M' corresponds to month, and 'D' corresponds to day, 'h' corresponds
        to hour, 'm' corresponds to minute, and 's' corresponds to second.
        
    Returns:
        datetime.datetime object
    '''
    
    # Identify positions of date components from user-provided formatting.
    yr_pos = substring_position(string = form, substring = 'Y')
    mo_pos = substring_position(string = form, substring = 'M')
    dy_pos = substring_position(string = form, substring = 'D')
    hr_pos = substring_position(string = form, substring = 'h')
    mi_pos = substring_position(string = form, substring = 'm')
    sc_pos = substring_position(string = form, substring = 's')
    
    # Store date components.
    year = str()
    month = str()
    day = str()
    hour = str()
    minute = str()
    second = str()
    
    for i in yr_pos:
        year = year + date_time[i]
    
    for j in mo_pos:
        month = month + date_time[j]
    
    for k in dy_pos:
        day = day + date_time[k]
    
    for l in hr_pos:
        hour = hour + date_time[l]
    
    for m in mi_pos:
        minute = minute + date_time[m]
    
    for n in sc_pos:
        second = second + date_time[n]
    
    return datetime.datetime(year = int(year), month = int(month),
                             day = int(day), hour = int(hour),
                             minute = int(minute), second = int(second))

def add_date(df, date_column, date_form, new_column_name):
    df[new_column_name] = df.apply(
        lambda x: parse_date(
            date = x[date_column],
            form = date_form
            ),
        axis = 1
        )
    
def add_time(df, time_column, time_form, new_column_name):
    df[new_column_name] = df.apply(
        lambda x: parse_time(
            time = x[time_column],
            form = time_form
            ),
        axis = 1
        )

def add_date_time(df, date_time_column, date_time_form, new_column_name):
    df[new_column_name] = df.apply(
        lambda row: parse_date_time(
            date_time = row[date_time_column],
            form = date_time_form
            ),
        axis = 1
        )

def add_isoweekday_from_date_time(df, date_time_column, new_column):
    df[new_column] = df.apply(
        lambda row: row[date_time_column].isoweekday(),
        axis = 1
        )

def add_time_from_date_time(df, date_time_column, new_column):
    df[new_column] = df.apply(
        lambda row: row[date_time_column].time(),
        axis = 1
        )

def standardize_by_time(df, date_time_column = None, time_column = None):
    
    # Ensure column name is formatted correctly for merge.
    if type(date_time_column) == str:
        df['Time'] = df.apply(
            lambda row: row[date_time_column].time(),
            axis = 1
            )
    elif type(time_column) == str:
        df['Time'] = df[time_column]
    else:
        sys.exit('ERROR: A column must be supplied.')
    
    # Create a list that corresponds to every second in the day.
    l = list()
    for i in range(24):
        for j in range(60):
            for k in range(60):
                l.append(datetime.time(hour = i, minute = j, second = k))
    
    # Create a dataframe that will hold the result and assign the list to it.
    r = pd.DataFrame(index = np.arange(86400), columns=np.arange(0))
    r['Time'] = l
    
    # Merge the dateframes.
    r = r.merge(right = df, how = 'left')
    
    return r

def average_over_interval(df, column, interval):
    
    if (86400/interval).is_integer():
        # Generate dataframe to hold results.
        nrow = int(86400/interval)
        r = pd.DataFrame(index = np.arange(nrow), columns=np.arange(0))
        
        # Create list that holds aggregated data.
        l = list()
        for i in range(nrow):
            lower = 0 + (i * interval)
            upper = interval + (i * interval)
            l.append(st.mean(df[column][lower:upper]))
        
        # Create list that holds time.
        t = list()
        for i in range(nrow):
            time_change = datetime.timedelta(seconds = (interval*i))
            time = datetime.datetime(1900,1,1,0,0,0) + time_change
            t.append(time.time())
        
        # Create time column and store averaged data.
        r['Time'] = t
        r[column] = l
    else:
        sys.exit('ERROR: Seconds per day must be divisible by interval.')
    
    return r

def assign_vehicle_state(df, time_column, speed_column, spd_thr, str_thr=1, end_thr=1):
    # Create a temporary dataframe that artificially contains three days of data.
    nobs = len(df)
    nrow = len(df)*3
    temp = pd.DataFrame(index = np.arange(nrow), columns=np.arange(0))
    temp['Time'] = list(df[time_column]) + list(df[time_column]) + list(df[time_column])
    temp['Speed'] = list(df[speed_column]) + list(df[speed_column]) + list(df[speed_column])
    
    # Process data according to specified rules.
    temp['Boolean'] = temp.apply(
        lambda row: row['Speed'] > spd_thr, axis = 1
        )
    
    temp['State'] = None
    for i in range(nobs,nobs*2):
        if temp.loc[i,'Boolean'] == True:
            if sum(temp.loc[(i-str_thr):(i-1),'Boolean']) == 0 and sum(temp.loc[(i+1):(i+1),'Boolean']) >= 1:
                temp.loc[i,'State'] = 'STARTING'
            elif sum(temp.loc[(i-1):(i-1),'Boolean']) >= 1 and sum(temp.loc[(i+1):(i+end_thr),'Boolean']) == 0:
                temp.loc[i,'State'] = 'ENDING'
            elif sum(temp.loc[i:i,'Boolean']) == 1:
                temp.loc[i,'State'] = 'OPERATING'
        else:
            temp.loc[i,'State'] = 'DEPOT'
            
    # Generate dataframe to hold results.
    r = pd.DataFrame(index = np.arange(nobs), columns=np.arange(0))
    r['Time'] = list(temp['Time'][nobs:(nobs*2)])
    r['State'] = list(temp['State'][nobs:(nobs*2)])
    
    return r

def return_file_list(root_dir, file_level = 1, filter_term = ''):
    
    if file_level == 1:
        file_list = glob.glob(pathname = os.path.join(root_dir,'*' + filter_term), recursive = True)
    elif file_level == 2:
        file_list = glob.glob(pathname = os.path.join(root_dir,'*','*' + filter_term), recursive = True)
    elif file_level == 3:
        file_list = glob.glob(pathname = os.path.join(root_dir,'*','*','*' + filter_term), recursive = True)
    elif file_level == 4:
        file_list = glob.glob(pathname = os.path.join(root_dir,'*','*','*','*' + filter_term), recursive = True)
    elif file_level == 5:
        file_list = glob.glob(pathname = os.path.join(root_dir,'*','*','*','*','*' + filter_term), recursive = True)
    else:
        return sys.exit('The variable "file_level" must be a number between 1 and 5.')
    
    return file_list
    
def parse_variables(text, form):

    
    # Identify positions of date components from user-provided formatting.
    veh_pos = substring_position(string = form, substring = 'V')
    voc_pos = substring_position(string = form, substring = 'O')
    wgt_pos = substring_position(string = form, substring = 'W')
    eng_pos = substring_position(string = form, substring = 'E')
    y_pos = substring_position(string = form, substring = 'Y')
    m_pos = substring_position(string = form, substring = 'M')
    d_pos = substring_position(string = form, substring = 'D')
    
    # Store variable components.
    vid = str()
    voc = str()
    wgt = str()
    eng = str()
    yea = str()
    mon = str()
    day = str()

    
    for i in y_pos:
        yea = yea + text[i]
    
    for i in m_pos:
        mon = mon + text[i]
    
    for i in d_pos:
        day = day + text[i]
    
    for i in veh_pos:
        vid = vid + text[i]
    
    for i in voc_pos:
        voc = voc + text[i]
    
    for i in wgt_pos:
        wgt = wgt + text[i]
    
    for i in eng_pos:
        eng = eng + text[i]

    dat = datetime.date(year = int(yea),
                         month = int(mon),
                         day = int(day))

    var_list = list()
    var_list.append(vid)
    var_list.append(voc)
    var_list.append(wgt)
    var_list.append(eng)
    var_list.append(dat)
    
    return var_list

def is_numeric(x):
    if type(x) == int:
        return True
    elif type(x) == float:
        return True
    elif type(x) == str and x.isnumeric():
        return True
    else:
        return False

def summarize_state_variables(df, time_col, state_col):
    
    str_table = pd.DataFrame(df.loc[df[state_col] == 'STARTING', time_col])
    end_table = pd.DataFrame(df.loc[df[state_col] == 'ENDING', time_col])
    str_count = len(str_table)
    end_count = len(end_table)
    
    max_count = max(str_count,end_count)
    
    df_sum = pd.DataFrame()
    
    df_sum['Start_Count'] = [str_count]
    df_sum['End_Count'] = [end_count]
    
    for i in range(max_count):
        try:
            df_sum['Start_'+str(i+1).zfill(2)] = str_table.iloc[i,0].hour + (str_table.iloc[i,0].minute / 60)
        except:
            df_sum['Start_'+str(i+1).zfill(2)] = -99
    
    for i in range(max_count):
        try:
            df_sum['End_'+str(i+1).zfill(2)] = end_table.iloc[i,0].hour + (end_table.iloc[i,0].minute / 60)
        except:
            df_sum['End_'+str(i+1).zfill(2)] = -99
    
    return df_sum
    
def calculate_distance(df, interval, speed_col):
    distance_table = (df[speed_col] / 3600) * interval
    distance = sum(distance_table)
    
    return distance
        
def process_telematics_from_directory(directory, file_level, var_format,
                                      speed_col, new_speed_col,
                                      time_col, time_format, new_time_col,
                                      spd_thr = 0.01, str_thr = 1, end_thr =1,
                                      interval = (15*60)):
    
    # Normalize the file pathway.
    direct = os.path.normpath(directory)
    
    # Create a list that contains every file that will be looped through.
    all_files = return_file_list(root_dir = direct,
                                  file_level = file_level,
                                  filter_term = '.csv')
    
    # Create a table the will be used to hold variables for each of the files.
    var_df = pd.DataFrame(columns=['Vehicle_ID','Vocation','Weight_Class','Engine','Date'])
    
    for i in range(len(all_files)):
        var = parse_variables(text = all_files[i], form = var_format)
        var_df.loc[len(var_df)] = var
    
    # Add ISO day of the week to the dataframe.
    add_isoweekday_from_date_time(df = var_df,
                                  date_time_column = 'Date',
                                  new_column = 'ISO_Day')
    
    for i in range(len(all_files)):
        # Read CSV file.
        df1 = pd.read_csv(all_files[i])
        
        # Add time column as a date-time object.
        add_time(df = df1, time_column = time_col, time_form = time_format,
                  new_column_name = new_time_col)
        
        
        # Standardize the dataset so that it includes a full 86400-second day.
        df2 = standardize_by_time(df = df1, time_column = new_time_col)
        
        # Fill any non-numeric values.
        df2[new_speed_col] = df2[speed_col].fillna(0)
        
        # Calculate total distance driven in this observation day.
        dist = calculate_distance(df = df2, interval = 1, speed_col = new_speed_col)
        
        # Average speed over the interval provided.
        df3 = average_over_interval(df = df2, column = new_speed_col,
                                    interval = interval)
        
        # Assign vehicle state based on the averaged interval data.
        df4 = assign_vehicle_state(df = df3, time_column = new_time_col,
                                    speed_column = new_speed_col,
                                    spd_thr = spd_thr, str_thr = str_thr,
                                    end_thr = end_thr)
        
        if i == 0:
            rdf1 = df4
        else:
            rdf1 = pd.concat([rdf1,df4['State']], axis = 1)
        
        # Summarize key variables related to operational state of the vehicles.
        if i == 0:
            df5 = summarize_state_variables(df = df4, time_col = new_time_col,
                                        state_col = 'State')
        
            df5.loc[i,'Distance'] = dist
        else:
            df5 = df5.append(summarize_state_variables(df = df4,
                                                        time_col = new_time_col,
                                                        state_col = 'State'))
            
            df5 = df5.reset_index(drop = True)
            
            df5.loc[i,'Distance'] = dist
    
    df5 = df5.reindex(sorted(df5.columns), axis = 1)
    
    # Combine parsed variables with state variables and distance.
    rdf2 = pd.concat([var_df, df5], axis = 1)
        
    return rdf1, rdf2
    

# TEST #



# x,y = process_telematics_from_directory('G:/My Drive/EDF/Data/01_Source/drayagesocal.00',
#                                   2,
#                                   '________________________________________________________VVVVV_EEE_WW_OOOOOOO___________YYYY_MM_DD____','GpsSpeed','Speed',
#                                   'DateTime_Logger_UTC','YYYY-MM-DD hh:mm:ss-__:__','Time')

x = process_telematics_from_directory('G:\\My Drive\\EDF\\Data\\01_Source\\cngsocal.00',
                                      4,
                                      '______________________________________________________________________________________________________________VVVVV_EEE_WW_OOOOOOO______________________________YYYY_MM_DD____',
                                      'GpsSpeed','Speed',
                                      'DateTime_Logger_UTC','YYYY-MM-DD hh:mm:ss-__:__','Time')

# Replace this file name with whatever file path you use.
# df1 = pd.read_csv('G:/My Drive/EDF/Data/01_Source/drayagesocal.00/2015.c1.t12127.ice.08.drayage/I35_12127_2015-06-16.csv')

# add_date_time(df1,'DateTime_Logger_UTC','YYYY-MM-DD hh:mm:ss-__:__','Date_Time')

# add_time(df1,'DateTime_Logger_UTC','YYYY-MM-DD hh:mm:ss-__:__','Time')

# df2 = standardize_by_time(df1, time_column='Time')

# df2['GpsSpeed'] = df2['GpsSpeed'].fillna(0)

# df3 = average_over_interval(df2, column = 'GpsSpeed', interval = (60*15))

# dff = assign_vehicle_state(df = df3, time_column='Time',speed_column='GpsSpeed',spd_thr=0.01,str_thr=1,end_thr=1)

# tes = merge_by_time(df, date_time_column='Date_Time')

# df2 = df1.merge(right = df, how = 'left', on = )