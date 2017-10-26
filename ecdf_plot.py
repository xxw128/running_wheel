"""
1. Takes tidy data as input, plot ECDF for each individual mice.
"""


import pandas as pd
import numpy as np

import bootcamp_utils

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

import sys
fname = sys.argv[1]

df = pd.read_csv(fname)
df.index = df['time']

#slicing by genotype: dwt and dko, then by lightdark
dwt = df.loc[df['group']=='wt', :]
dko = df.loc[df['group']=='DKO',:]

dwt_dark = dwt.loc[dwt['lightdark']=='dark', ['group','mouse_id','lightdark', 'rev_in_1hr']]
dwt_light = dwt.loc[dwt['lightdark']=='light', ['group','mouse_id','lightdark', 'rev_in_1hr']]
dko_dark = dko.loc[dko['lightdark']=='dark', ['group','mouse_id','lightdark', 'rev_in_1hr']]
dko_light = dko.loc[dko['lightdark']=='light', ['group','mouse_id','lightdark', 'rev_in_1hr']]

#slicing by light/dark
df_light = df.loc[df['lightdark']=='light', :]
df_dark = df.loc[df['lightdark']=='dark', :]


# Set up figure for dark hours
fig, ax = plt.subplots(3, 1, figsize=(6, 12))
ax[0].set_xlabel('activity (rev/hr)')
ax[0].set_ylabel('ECDF')
ax[0].set_title('NtaQ1+/+;NtaN1+/+')
ax[1].set_xlabel('activity (rev/hr)')
ax[1].set_ylabel('ECDF')
ax[1].set_title('NtaQ1-/-;NtaN1-/-')
ax[2].set_xlabel('activity (rev/hr)')
ax[2].set_ylabel('ECDF')
ax[2].set_title('Dark')

# Plot ECDFs for dark hours: [0] wt_individual [1] DKO_individual [2] pooled within genotypes
ax[0] = bootcamp_utils.ecdf_plot(dwt_dark, 'rev_in_1hr',
                                 hue='mouse_id', ax=ax[0])
ax[1] = bootcamp_utils.ecdf_plot(dko_dark, 'rev_in_1hr',
                                 hue='mouse_id', ax=ax[1])
ax[2] = bootcamp_utils.ecdf_plot(df_dark, 'rev_in_1hr',
                                 hue='group', ax=ax[2])

# tight_layout makes sure axis labels, etc., to not overlap
fig.tight_layout(h_pad=3)
plt.savefig('ECDF_dark.pdf')

# Set up figure for light hours
fig, ax = plt.subplots(3, 1, figsize=(6, 12))
ax[0].set_xlabel('activity (rev/hr)')
ax[0].set_ylabel('ECDF')
ax[0].set_title('NtaQ1+/+;NtaN1+/+')
ax[1].set_xlabel('activity (rev/hr)')
ax[1].set_ylabel('ECDF')
ax[1].set_title('NtaQ1-/-;NtaN1-/-')
ax[2].set_xlabel('activity (rev/hr)')
ax[2].set_ylabel('ECDF')
ax[2].set_title('Light')

# Plot ECDFs for light hours
ax[0] = bootcamp_utils.ecdf_plot(dwt_light, 'rev_in_1hr',
                                 hue='mouse_id', ax=ax[0])
ax[1] = bootcamp_utils.ecdf_plot(dko_light, 'rev_in_1hr',
                                 hue='mouse_id', ax=ax[1])
ax[2] = bootcamp_utils.ecdf_plot(df_light, 'rev_in_1hr',
                                 hue='group', ax=ax[2])
# tight_layout makes sure axis labels, etc., to not overlap
fig.tight_layout(h_pad=3)
plt.savefig('ECDF_light.pdf')

plt.show()
