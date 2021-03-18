# Numerical Analysis
import io_layer as io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn


#data = io.read_in_df(filedir, filename)
#alternatively defining data once and then only read in data for the other functions?

def expect_plot(filedir, filename, threshv):
    """expec
    need: filedir, filename, threshv
    reads in the dataframe file
    drops data above threshold
    plots relevant data
    """
    df_expec = io.read_in_df(filedir, filename)
    df_expec.drop(df_expec.var()[df_expec.var() < threshv].index.values, axis=1)
    sn.relplot(df_expec, kind='line')
    plt.show()
    return

def npop_plot(filedir, filename, threshv):
    """ npop_plot

    Args:
        filedir - directory of the dataframe file
        filename - name of the dataframe file
        threshv - threshold value for the sorting

    Return:
        plots of the sorted data"""

    df_npop = io.read_in_df(filedir, filename)
    df_npop2 = df_npop.drop(df_npop.var()[df_npop.var() < threshv].index.values, axis=1)
    sn.lineplot(x='time', y='value', hue='MO', data=df_npop2)
    plt.show()
    return

#npop_plot('../../data/', 'npop.t', 0.000001)

def npop_corr(filedir, filename, threshv):
    df_npop = io.read_in_df(filedir, filename)
    df_npop2_short = df_npop.drop(df_npop.var()[df_npop.var() < threshv].index.values, axis=1)
    value_list = set()
    column_names = df_npop2_short.columns
    for i in range(0, df_npop2_short.shape[1]):
        for j in range(0, i+1):
            value_list.add((column_names[i], column_names[j]))
    final_correlation = df_npop2_short.corr().unstack()
    final_correlation = final_correlation.drop(labels=value_list).sort_values(ascending=False, key=lambda col: col.abs())
    print(final_correlation)
    return

npop_corr('~/ssc_course_team4/data/', 'npop.t', 0.000001)
#data = pd.read_csv('~/ssc_course_team4/data/npop.t', r'\s+')
