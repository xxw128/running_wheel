# In our IPython terminal do:
# %matplotlib

#to run the code in IPython
# %run plot_by_date.py '2017_0628_tidy_data.csv'

import numpy as np
import pandas as pd
import datetime
import wheel_utils

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

import sys
filename = sys.argv[1]
# Read in data
data = pd.read_csv(filename)

#Split data into sub dataframes by group
data_1 = data.loc[data['group']=='saline', :]
data_2 = data.loc[data['group']=='lps-2', :]
data_3 = data.loc[data['group']=='lps-5', :]
data_4 = data.loc[data['group']=='lps-10', :]

# Set up plot area
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(15,7.5), sharex=True)

# Plot each group
ax1.set_ylabel('Rev in 1 hr')
ax1.set_title('Saline')
ax1 = wheel_utils.time_plot(data_1, 'rev_in_1hr', hue='mouse_id', ax=ax1)

ax2.set_ylabel('Rev in 1 hr')
ax2.set_title('LPS-2mg/ml')
ax2 = wheel_utils.time_plot(data_2, 'rev_in_1hr', hue='mouse_id', ax=ax2)

ax3.set_ylabel('Rev in 1 hr')
ax3.set_title('LPS-5mg/ml')
ax3 = wheel_utils.time_plot(data_3, 'rev_in_1hr', hue='mouse_id', ax=ax3)

ax4.set_ylabel('Rev in 1 hr')
ax4.set_title('LPS-10mg/ml')
ax4 = wheel_utils.time_plot(data_4, 'rev_in_1hr', hue='mouse_id', ax=ax4)

plt.show()
