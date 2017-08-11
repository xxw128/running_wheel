import pandas as pd
import datetime
import numpy as np

"""
Shift time to relative of surgery date
mouse_id 11-18: surgery between 2017-07-10 11:15:00 and 2017-07-10 15:25:00'
mouse_id 19-22: surgery between 2017-07-11 11:00:00 and 2017-07-10 14:30:00'
"""

# Read in the file. Delete the duplicate 'time.1' column.
# Convert 'time' to datetime object
import sys
filename = sys.argv[1]
all_data = pd.read_csv(filename)
all_data = all_data.loc[ : , ['time', 'group', 'mouse_id', 'sensor_type',
                          'rev_in_1hr','lightdark'] ]
all_data['time'] = pd.to_datetime(all_data['time'])

# define groups and surgery days
group1 = range(11, 19)
surgery_day1 = pd.to_datetime('2017-07-10 00:00:00')
group2 = range(19, 23)
surgery_day2 = pd.to_datetime('2017-07-11 00:00:00')

# Slicing data according to groups
data_1 = all_data.loc[all_data['mouse_id'].isin(group1), :]
data_2 = all_data.loc[all_data['mouse_id'].isin(group2), :]

# Calculate timedelta comparing to surgery day
data_1['post_op'] = data_1['time'] - surgery_day1
data_2['post_op'] = data_2['time'] - surgery_day2

new_data = pd.concat([data_1, data_2])

output_name = filename.split('.')[0] + '_relativetime.csv'
new_data.to_csv(output_name, index=False)
