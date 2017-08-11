# Plotting modules and settings.

import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


def extract_xy(data, value):
    """
    Compute 'x' and 'y' values for x-y plot.
    'x' axis is time. 'y' is usually activity (wheel rev per hour)

    Parameters
    ----------
    data : array_like
        Array of data to be plotted as an x-y plot.

    Returns
    -------
    x : array
    'x' values for plotting.
    y : array
        `y` values for plotting
    """

    return pd.to_datetime(data['time'], infer_datetime_format=True), data[value]



def time_plot(data, value, hue=None, ax=None):

    """
    Generate `x` and `y` values for plotting an x-y plot.

    Parameters
    ----------
    data : Pandas DataFrame
        Tidy DataFrame with data sets to be plotted.
    value : column name of DataFrame
        Name of column that contains data to make xy-plot with.
    hue : column name of DataFrame
        Name of column that identifies labels of data. A seperate
        line is plotted for each unique entry.
    ax : matplotlib Axes
        Axes object to draw the plot onto, otherwise makes a new
        figure/axes.

    Returns
    -------
    output : matplotlib Axes
        Axes object containg ECDFs.
    """

    # Set up axes
    if ax is None:
        fig, ax = plt.subplots(1, 1)
        ax.set_xlabel('time')
        ax.set_ylabel(str(value))

    if hue is None:
        x,y = extract_xy(data,value)

        # Make plots
        _ = ax.plot(x, y, marker='.')
    else:
        gb = data.groupby(hue)
        xys = gb.apply(extract_xy, value)

        # Make plots
        for i, xy in xys.iteritems():
            _ = ax.plot(*xy, marker='.', )

        # Add Legend
        ax.legend(xys.index, loc=0)

    return ax
