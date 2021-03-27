import numpy as np
import pandas as pd
import src.ssc_course_team4.io_layer as io
import seaborn as sn
import matplotlib.pyplot as plt


def expect_plot(filepath_in, threshv):
    """Reads in dataframe file, drops data with variance below threshold and
    plots relevant data.

    Args:
            filepath_in (str): input file location
            thresv (double): desired threshold value

    Return:
    """
    df_expec = io.read_in_df(filepath_in)
    df_expec2 = df_expec.drop(df_expec.var()
                            [df_expec.var() < threshv].index.values, axis=1)
    sn.relplot(x='time', y='value', hue='variable',
                data=pd.melt(df_expec2, ['time']), kind='line')
    plt.show()
    return


def npop_plot(filepath_in, threshv):
    """ Reads in dataframe file, drops data with variance below threshold and
            plots relevant data.

    Args:
            filepath_in (str): input file location
            thresv (double): desired threshold value
    Return:
            relplots of the relevant data
    """

    df_npop = io.read_in_df(filepath_in)
    df_npop2 = df_npop.drop(
                df_npop.var()[df_npop.var() < threshv].index.values, axis=1)
    sn.lineplot(x='time', y='value',
                hue='variable', data=pd.melt(df_npop2, ['time']))
    plt.show()
    return


def npop_corr(df_npop, threshv):
    """ Reads in dataframe file, drops data with variance below threshold and
        redundant entries, sorts for absolute correlation values and prints it
        to npop_corr.cvs

    Args:
            filepath_in (str): input file location
            filepath_out (str): output file location
            thresv (double): desired threshold value
    Return: npop_corr.cvs file with sorted, non-redundant correlation values
    """
    df_npop2_short = df_npop.drop(columns='time')  # ToDo: Added, check if ok
    df_npop2_short = df_npop2_short.drop(
                df_npop.var()[df_npop.var() < threshv].index.values, axis=1)
    value_list = set()
    column_names = df_npop2_short.columns
    for i in range(0, df_npop2_short.shape[1]):
        for j in range(0, i+1):
            value_list.add((column_names[i], column_names[j]))
    final_correlation = df_npop2_short.corr().unstack()
    final_correlation = final_correlation.drop(labels=value_list).sort_values(
                                ascending=False, key=lambda col: col.abs())

    return final_correlation


def euclid_dis(table, thresh):
    """Calculates the Euclidean distance for two vektors.

    Args:
        table (numpy array): Numpy array of the vektor data (i,j, r(x), v(x),
                            r(y), v(y), r(z), v(z), skiprow=1).
        thresh (double integer): The threshhold value that the data should be
            checked against.

    Returns:
    """
#   Remove NaN and remove that column
    np.nan_to_num(table, False, 0)
    table = np.delete(table, 0, 0)

#   Calculate Euclidean Distance per axis
    result_x = np.sqrt(np.sum((table[:, 2]-table[:, 3])**2))
    result_y = np.sqrt(np.sum((table[:, 4]-table[:, 5])**2))
    result_z = np.sqrt(np.sum((table[:, 6]-table[:, 7])**2))
    result = result_x, result_y, result_z

    return result
