"""
Title: VTP Functions

Description: The VTP package contains functions for processing
vehicle telematics data and applying deterministic rules to
characterize a vehicle's activity.

Author: Alexander Yoshizumi

Last Updated: 14 January 2024

"""

# ---------------------------------------------------------------------------
# Required Packages
# ---------------------------------------------------------------------------
import datetime
import pandas as pd
import numpy as np
import statistics as st
import sys
import os
import glob

# ---------------------------------------------------------------------------
# VTP Package Functions
# ---------------------------------------------------------------------------
def substring_position(string, substring):
    '''
    Description:
    A function that indicates at what position in a string a substring occurs.

    Attributes:
        string: The larger string that is being searched. 
        substring: The shorter string that serves as the search term.
        
    Returns:
        list object with position integer
    '''
    r = [i for i in range(len(string)) if string.startswith(substring, i)]
    return r

def parse_date(date, form):
    '''
    Description:
    A function that extracts the year, month, and day from a date string.
    This function only works with numeric date values (e.g., 2020-01-30,
    01/30/2020, etc.)

    Attributes:
        date: The string containing the date of interest.
        form: The format of the date text string where "Y" corresponds to year,
        "M" corresponds to month, and "D" corresponds to day.
        
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
    A function that extracts the hour, minute, and second from a time string.

    Attributes:
        time: The string containing the time of interest.
        form: The format of the time text string where "h" corresponds to hour,
        "m" corresponds to minute, and "s" corresponds to second.
        
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
    A function that extracts the year, month, day, hour, minute, and second from a date-time string.
    This function only works with numeric date values (e.g., 2020-01-30,
    01/30/2020, etc.)

    Attributes:
        date_time: The string containing the date and time of interest.
        form: The format of the date-time text string where "Y" corresponds
        to year, "M" corresponds to month, "D" corresponds to day, "h" corresponds
        to hour, "m" corresponds to minute, and "s" corresponds to second.
        
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
    '''
    Description:
    A function that adds a new date column with date stored as a datetime.date object.
    This function only works with numeric date values (e.g., 2020-01-30,
    01/30/2020, etc.)

    Attributes:
        df: The dataframe being modified.
        date_column: The existing column containing the date.
        date_form: The format of the date text string where "Y" corresponds to year,
        "M" corresponds to month, and "D" corresponds to day. The user must specify
        all parts of the text in the date_form variable. For example, the date format
        for "VID23045_20200130_CNG" would be "+++++++++YYYYMMDD++++". The characters used
        as filler do not matter so long as they are not a reserved character (i.e., "Y",
        "M", or "D").
        new_column_name: The name to be assigned to the new column.
        
    Returns:
        the input dataframe with a new column that indicates date
    '''

    df[new_column_name] = df.apply(
        lambda x: parse_date(
            date = x[date_column],
            form = date_form
            ),
        axis = 1
        )
    
def add_time(df, time_column, time_form, new_column_name):
    '''
    Description:
    A function that adds a new time column with time stored as a datetime.time object.

    Attributes:
        df: The dataframe being modified.
        time_column: The existing column containing the date.
        time_form: The format of the time text string where "h" corresponds to hour,
        "m" corresponds to minute, and "s" corresponds to second. The user must specify
        all parts of the text in the time_form variable. For example, the time format
        for "12:42:30" would be "hh+mm+ss". The characters used as filler do not matter
        so long as they are not a reserved character (i.e., "h", "m", or "s").
        new_column_name: The name to be assigned to the new column.
        
    Returns:
        the input dataframe with a new column that indicates time
    '''
        
    df[new_column_name] = df.apply(
        lambda x: parse_time(
            time = x[time_column],
            form = time_form
            ),
        axis = 1
        )

def add_date_time(df, date_time_column, date_time_form, new_column_name):
    '''
    Description:
    A function that adds a new date-time column with the date-time stored as
    a datetime.datetime object.

    Attributes:
        df: The dataframe being modified.
        date_time_column: The existing column containing the date.
        date_time_form: The format of the date-time text string where "Y" corresponds to
        year, "M" corresponds to month, "D" corresponds to day, "h" corresponds to hour,
        "m" corresponds to minute, and "s" corresponds to second. The user must specify
        all parts of the text in the time_form variable. For example, the date-time format
        for "2020-01-30_12:42:30" would be "YYYY+MM+DD+hh+mm+ss". The characters used as
        filler do not matter so long as they are not a reserved character (i.e., "Y",
        "M", "D", "h", "m", or "s").
        new_column_name: The name to be assigned to the new column.
        
    Returns:
        the input dataframe with a new column that indicates date-time
    '''
    df[new_column_name] = df.apply(
        lambda row: parse_date_time(
            date_time = row[date_time_column],
            form = date_time_form
            ),
        axis = 1
        )

def add_isoweekday_from_date_time(df, date_time_column, new_column):
    '''
    Description:
    A function that adds a new column which specifies which day of the week
    corresponds to an observations given date-time. The ISO week starts on Monday,
    so a value of 1 corresponds to Monday and a value of 7 corresponds to Sunday.

    Attributes:
        df: The dataframe being modified.
        date_time_column: The existing column containing the date-time.
        new_column_name: The name to be assigned to the new column.
        
    Returns:
        the input dataframe with a new column that indicates day of the week
    '''
    df[new_column] = df.apply(
        lambda row: row[date_time_column].isoweekday(),
        axis = 1
        )

def add_time_from_date_time(df, date_time_column, new_column):
    '''
    Description:
    A function that adds a new column and populates the new column with
    a datetime.time objects extracted from an initial column that is already
    populated with datetime.datetime objects. 

    Attributes:
        df: The dataframe being modified.
        date_time_column: The existing column containing the date-time.
        new_column_name: The name to be assigned to the new column.
        
    Returns:
        the input dataframe with a new column that indicates time
    '''
    df[new_column] = df.apply(
        lambda row: row[date_time_column].time(),
        axis = 1
        )

def standardize_by_time(df, date_time_column = None, time_column = None):
    '''
    Description:
    A function that standardizes an input telematics dataframe into a dataframe
    that has a row for every second of vehicle operation. This results in a
    dataframe with 86,400 rows. 

    Attributes:
        df: The input dataframe.
        date_time_column: The existing column containing the date-time.
        time_column: The existing column containing the time.
        
    Returns:
        a new dataframe that standardizes the input dataframe by merging the
        original dataframe observations into a table with rows for every
        second of the day
    '''    
    
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
    '''
    Description:
    A function that averages column values over a specified interval. The
    interval is measured in seconds.

    Attributes:
        df: The input dataframe.
        column: The column being averaged.
        interval: The interval to average over measured in seconds.
        
    Returns:
        a new dataframe that contains averaged values over the specified
        time interval.
    '''    

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
    '''
    Description:
    A function that assigns a vehicle state based on rules specified by the user.
    This function breaks down fleet vehicle behavior into four states:
    (1) Starting, (2) Operating, (3) Ending, and (4) Depot.

    Attributes:
        df: The input dataframe.
        time_column: The column containing time values.
        speed_column: The column containing speed values.
        spd_thr: The speed threshold at which a vehicle is considered active.
        The value should correspond to the units used in the input data.
        str_thr: The threshold that indicates how long a vehicle must be at rest
        before activity to be considered "STARTING". Being at rest refers to
        non-activity as determined by the spd_thr variable. This value is measured
        in observations/rows.
        end_thr: The threshold that indicates how long a vehicle must be at rest
        after activity to be considered "ENDING". This value is measured in
        observations/rows.
        
    Returns:
        a new dataframe that contains vehicle states by time.
    '''    

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
    '''
    Description:
    A function that can recursively search multiple folders down within a directory
    and produce a list of file names at a specified directory level. This function
    is useful for when files are organized into multiple cascading folders.

    Attributes:
        root_dir: The pathway to the folder of interest.
        file_level: The number of levels deep the files of interest are relative to
        the root_dir.
        filter_term: Users may supply a file extension type to filter results by.
        
    Returns:
        a list of file names
    '''    

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
    '''
    Description:
    A function that can extract key variables of interest from a text string.

    Attributes:
        text: The text containing coded information.
        form: The The format of the file string or other text where "V" corresponds to
        vehicle ID, "O" corresponds to occupation/vocation, "W" corresponds to weight
        class, "E" corresponds to engine/fuel type, "Y" corresponds to year, "M"
        corresponds to month, and "D" corresponds to day. The user must specify all
        parts of the text in the form variable. For example, the format string for
        for "2019.c1.t12181.ice.08.transit.2016-02-22.csv" would be
        "+++++++++VVVVV+EEE+WW+OOOOOOO+YYYY+MM+DD++++". The characters used as
        filler do not matter so long as they are not a reserved character (i.e., "V",
        "O", "W", "E", "Y", "M" or "D").
        
    Returns:
        a list of variables
    ''' 
    
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
    '''
    Description:
    A function that can flexibly determine if a value is numeric regardless of whether
    it is already in a numeric form or if it is a number in string form.

    Attributes:
        x: The input value.
        
    Returns:
        a boolean response of either True or False.
    ''' 
    if type(x) == int:
        return True
    elif type(x) == float:
        return True
    elif type(x) == str and x.isnumeric():
        return True
    else:
        return False

def summarize_state_variables(df, time_col, state_col):
    '''
    Description:
    A function that summarizes the state variables from a vehicle state dataframe
    Variables summarized include the number of starts, the number of ends, the hour
    of each start, and the hour of each end. The input must be a state variable chart
    as returned by the assign_vehicle_state() function.

    Attributes:
        df: The input vehicle state dataframe.
        time_col: The name of the time column.
        state_col: The name of the state column.
        
    Returns:
        a dataframe with columns associated with the count of starts, the count of
        ends, the time of each start measured in decimal hours, and the time of each
        end measured in decimal hours.
    ''' 
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
    '''
    Description:
    A function that calculates the total distance of all travel within a dataframe that
    has be standardized to a uniform time interval.  

    Attributes:
        df: The input dataframe.
        interval: The standard interval between observations measured in seconds.
        speed_col: The column name that corresponds to vehicle speed.
        
    Returns:
        a number that corresponds to the full distance traveled by the vehicle
        over the given observation day.
    ''' 

    distance_table = (df[speed_col] / 3600) * interval
    distance = sum(distance_table)
    
    return distance
        
def process_telematics_from_directory(directory, file_level, var_format,
                                      speed_col, new_speed_col,
                                      time_col, time_format, new_time_col,
                                      file_filter_term = '.csv',
                                      spd_thr = 0.01, str_thr = 1, end_thr =1,
                                      interval = (15*60)):
    '''
    Description:
    A function that processes all observation-day telematics files within a given
    directory. The function results in two dataframe tables: one dataframe contains
    operating states for every observation-day file where each file corresponds to 
    a unique column, the other dataframe corresponds to key variables related to
    each observation-day file that can be used to cluster the data by duty cycle. 
    
    Attributes:
        directory: The principal folder within which all files or cascading folders
        are held.
        file_level: The number of folder levels - if any - that must be cascaded
        through to arrive at the files of interest.  
        var_format: The The format of the file string or other text where "V" corresponds to
        vehicle ID, "O" corresponds to occupation/vocation, "W" corresponds to weight
        class, "E" corresponds to engine/fuel type, "Y" corresponds to year, "M"
        corresponds to month, and "D" corresponds to day. The user must specify all
        parts of the text in the form variable. For example, the format string for
        for "2019.c1.t12181.ice.08.transit.2016-02-22.csv" would be
        "+++++++++VVVVV+EEE+WW+OOOOOOO+YYYY+MM+DD++++". The characters used as
        filler do not matter so long as they are not a reserved character (i.e., "V",
        "O", "W", "E", "Y", "M" or "D").
        speed_col: The name of the speed column in the input files. 
        new_speed_col: The name to be assigned to the new speed column. This should be
        different from the original speed column name. 
        time_col: The name of the time column in the input files.
        time_format: The format of the time text string where "h" corresponds to hour,
        "m" corresponds to minute, and "s" corresponds to second. The user must specify
        all parts of the text in the time_form variable. For example, the time format
        for "12:42:30" would be "hh+mm+ss". The characters used as filler do not matter
        so long as they are not a reserved character (i.e., "h", "m", or "s").
        new_column_name: The name to be assigned to the new column.
        new_time_col: The name to be assigned to the new time column. This should be
        different from the original time column name.
        file_filter_term: The user may specify a file extension type to filter by. The
        default filter is ".csv". 
        spd_thr: The speed threshold at which a vehicle is considered active.
        The value should correspond to the units used in the input data. The default
        value is 0.01.
        str_thr: The threshold that indicates how long a vehicle must be at rest
        before being active in order to be considered "STARTING". Being at rest refers
        to non-activity as determined by the spd_thr variable. The default value is one.
        This value is measured in observations/rows.
        end_thr: The threshold that indicates how long a vehicle must be at rest
        after being active in order to be considered "ENDING". The default value is one.
        This value is measured in observations/rows.
        interval: The length of time over which vehicle activity is summarized in seconds.
        The default value is 900 seconds which corresponds to 15 minutes.
        
    Returns:
        (a) A dataframe containing operating states where each column corresponds to a processed file.
        (b) A dataframe with key variables that can be used to cluster the observations by duty cycle.
    '''
        
    # Normalize the file pathway.
    direct = os.path.normpath(directory)
    
    # Create a list that contains every file that will be looped through.
    all_files = return_file_list(root_dir = direct,
                                  file_level = file_level,
                                  filter_term = file_filter_term)
    
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