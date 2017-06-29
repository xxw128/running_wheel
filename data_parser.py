import numpy as np
import pandas as pd

import bootcamp_utils

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

import bokeh

# Load in the headers
with open('2017_0602_0626_qxn.csv') as fhandle:
    line_1 = fhandle.readline().rstrip()
    mouse_id = line_1.split(',')[1:len(line_1)]
    line_2 = fhandle.readline().rstrip()
    group = line_2.split(',')[1:len(line_2)]
    line_3 = fhandle.readline().rstrip()
    sensor_type = line_3.split(',')[1:len(line_3)]

# Load in the data to values_df
col_names= ['time'] + mouse_id
values_df = pd.read_csv('2017_0602_0626_qxn.csv', skiprows=3,
                        header=None, names=col_names)


# convert time to pd.datetime objects
time_parsed = pd.to_datetime(values_df['time'], format='%m/%d/%Y %I:%M:%S %p',
                             infer_datetime_format=True)
values_df['time'] = time_parsed

# DataFrame mouse_df to store mouse info
mouse_id = pd.Series(mouse_id)
group = pd.Series(group)
sensor_type = pd.Series(sensor_type)
mouse_df = pd.DataFrame({'mouse_id': mouse_id, 'group': group,
                        'sensor_type': sensor_type})

# Melt dataframe
values_df = pd.melt(values_df, id_vars='time', var_name='mouse_id',
                    value_name='activity(rev)')

# Merge with mouse_df
tidy_df = pd.merge(mouse_df,values_df)

# Write out DataFrame
tidy_df.to_csv('2017_0602_0626_qxn_tidy.csv', index=False)
