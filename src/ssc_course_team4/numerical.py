# Numerical Analysis
import io_layer as io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn


#data = io.read_in_df(filedir, filename)
#alternatively defining data once and then only read in data for the other functions?

def expect_plot(filedir, filename, threshv):
    """ reads in dataframe file, drops data with variance below threshold and plots relevant data

    Args:   filedir: directory of the dataframe file
            filename: name of the file
            thresv: desired threshold value

    Return: relplots of the relevant data
    """
    df_expec = io.read_in_df(filedir, filename)
    df_expec.drop(df_expec.var()[df_expec.var() < threshv].index.values, axis=1)
    sn.relplot(df_expec, kind='line')
    plt.show()
    return

def npop_plot(filedir, filename, threshv):
    """ reads in dataframe file, drops data with variance below threshold and plots relevant data

    Args:   filedir: directory of the dataframe file
            filename: name of the file
            thresv: desired threshold value

    Return: relplots of the relevant data
    """

    df_npop = io.read_in_df(filedir, filename)
    df_npop2 = df_npop.drop(df_npop.var()[df_npop.var() < threshv].index.values, axis=1)
    sn.lineplot(x='time', y='value', hue='variable', data=pd.melt(df_npop2, ['time']))
    plt.show()
    return

#npop_plot('~/ssc_course_team4/data/', 'npop.t', 0.00001)

def npop_corr(filedir, filename, threshv):
    """ reads in dataframe file, drops data with variance below threshold and redundant entries,
        sorts for absolute correlation values and prints it to npop_corr.cvs

    Args:   filedir: directory of the dataframe file
            filename: name of the file
            thresv: desired threshold value

    Return: npop_corr.cvs file with sorted, non-redundant correlation values
    """
    df_npop = io.read_in_df(filedir, filename)
    df_npop2_short = df_npop.drop(df_npop.var()[df_npop.var() < threshv].index.values, axis=1)
    value_list = set()
    column_names = df_npop2_short.columns
    for i in range(0, df_npop2_short.shape[1]):
        for j in range(0, i+1):
            value_list.add((column_names[i], column_names[j]))
    final_correlation = df_npop2_short.corr().unstack()
    final_correlation = final_correlation.drop(labels=value_list).sort_values(ascending=False, key=lambda col: col.abs())
    with open('npop_corr.cvs', 'w') as f:
        print(final_correlation, file=f)
    return

npop_corr('~/ssc_course_team4/data/', 'npop.t', 0.000001)
