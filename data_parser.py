import numpy as np
import pandas as pd


def lightdark(data):

    """Determine light/dark condition based on time index"""

    data.loc[data.index.hour.isin(range(7,20)), 'lightdark'] = 'light'
    data.loc[data.index.hour.isin([20,21,22,23,0,1,2,3,4,5,6]), 'lightdark'] = 'dark'
    return data


# define file to be processed
import sys
fname = sys.argv[1]

# Load in the headers
with open(fname) as fhandle:
    line_1 = fhandle.readline().rstrip()
    mouse_id = line_1.split(',')[1:len(line_1)]
    line_2 = fhandle.readline().rstrip()
    group = line_2.split(',')[1:len(line_2)]
    line_3 = fhandle.readline().rstrip()
    sensor_type = line_3.split(',')[1:len(line_3)]

# Load in the data to values_df
col_names= ['time'] + mouse_id
values_df = pd.read_csv(fname, skiprows=3,
                        header=None, names=col_names)

# DataFrame mouse_df to store mouse info
mouse_id = pd.Series(mouse_id)
group = pd.Series(group)
sensor_type = pd.Series(sensor_type)
mouse_df = pd.DataFrame({'mouse_id': mouse_id, 'group': group,
                        'sensor_type': sensor_type})

# use parsed time as index
time_parsed = pd.to_datetime(values_df['time'], format='%m/%d/%Y %I:%M:%S %p',
                             infer_datetime_format=True)
values_df['time'] = time_parsed
values_df.index = values_df['time']

#Resample
rule = '1h'
resampled_df = values_df.resample(rule, label='left').sum()
resampled_df['time'] = resampled_df.index

# Write DataFrame
prefix = fname.split('.')[0]
fout_mouse = prefix + '_mouse_info.csv'
fout_value = prefix + '_values.csv'
fout_resampled = prefix + '_values_' + rule + '.csv'
mouse_df.to_csv(fout_mouse, index=False)
values_df.to_csv(fout_value)
resampled_df.to_csv(fout_resampled)

# tidy data
melt_data = pd.melt(resampled_df, id_vars='time', var_name='mouse_id',
               value_name='rev_in_1hr')
merge_data = pd.merge(mouse_df, melt_data)
merge_data.index = merge_data['time']
tidy_data = lightdark(merge_data)
tidy_data.to_csv(prefix+'_tidy_data.csv')
