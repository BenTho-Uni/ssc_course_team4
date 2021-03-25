<<<<<<< HEAD
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
    df_expec2=df_expec.drop(df_expec.var()[df_expec.var() < threshv].index.values, axis=1)
    sn.relplot(x='time', y='value', hue='variable', data=pd.melt(df_expec2, ['time']), kind='line')
    plt.show()
    return

#example test run:
#expect_plot('~/ssc_course_team4/data/', 'expec.t', 0.00001)

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

#example test run:
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

#example test run:
#npop_corr('~/ssc_course_team4/data/', 'npop.t', 0.000001)
=======
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import src.ssc_course_team4.io_layer as io


def efield_fft(filepath_in, filepath_out, thresh):
    """Process and plots the electric field data and its Fourier-transformed
    function.

    Args:
        filepath_in (string): The relative file path to the data file.
        filepath_out (string): The relative file path where the output should
        be placed.
        thresh (double integer): The threshhold value that the data should be
            checked against.

    Returns:
    """
#   Read in efield data
    efield = io.read_in_df(filepath_in)
#   Plot efield per axis
    io.efield_plot(filepath_out, efield)
#   Drop those exis below threshhold
    efield_df = pd.DataFrame(efield)
    efield_df = efield_df.drop(efield_df.var()
                    [efield_df.var() < thresh].index.values, axis=1)
#   Convert to numpy array for easier Fourier
    efield_np = efield_df.to_numpy()
    efield_np = efield_np.T
#   Plot fft
    io.efield_fft_plot(filepath_out, efield_np)
    return


def autocorr(filepath_in):
    """Builds the autocorr. function as an array with a separated time array.

    Args:
        filepath_in (str): path to input file

    Returns:
        time: one dimensional numpy array with time steps
        corr: one dimensional numpy array with autocorrelation function
        value corresponding to the time step of the same index in the time
        array"""
    overlap = io.read_in_np(filepath_in)

    dim = len(overlap)
    time = np.zeros(dim)
    for i in np.arange(dim):
        time[i] = overlap[i][0]

    new_overlap = np.delete(overlap, 0, axis=1)

    index_real = [x for x in range(0, dim-1) if x % 2 == 0]
    index_complex = [x for x in range(0, dim-1) if not x % 2 == 0]

    real_arr = new_overlap[:, index_real]
    complex_arr = new_overlap[:, index_complex]

    overlap_c = real_arr + 1j * complex_arr

    corr_ = []
    for i in np.arange(0, dim):
        i = int(i)
        corr_.append(np.inner(np.conj(overlap_c[0]), overlap_c[i]))

    corr = np.array(corr_)

    return time, corr

def plot_autocorr(fielpath_in, filepath_out):
    """Builds the autocorrelation function as an array with a separated time
    array and plots the correlation function against time.

    Args:
        filepath_in (str): path to input file
        filepath_out (str): path to where the output file should be placed
        (columns must be separated by multiple spaces)

    Returns:
        autocorr_plot.pdf, but not as return"""
    time, corr = autocorr(fielpath_in)
    imag = np.imag(corr)
    real = np.real(corr)
    absolute = np.absolute(corr)

    plt.figure(1)
    fig_real, = plt.plot(time, real)
    fig_imag, = plt.plot(time, imag)
    fig_absolute, = plt.plot(time, absolute)
    plt.xlabel("time")
    plt.ylabel("overlap")
    plt.legend([fig_real, fig_imag, fig_absolute],
               ["real part", "imaginary part", "absolute value"],
               loc="center right")
    plt.savefig(filepath_out+"autocorr_plot.pdf")
    plt.show()

    return


def plot_autocorr_fft(filepath_in, filepath_out):
    """Builds the Fourier transform of the autocorrelation function as an
    array with a separated time array and plots the Fourier transform
    of the correlation function against time.

    Args:
        filepath_in (str): path to input file

    Returns:
        autocorr_fft_plot.pdf, but not as return"""
    time, corr = autocorr(filepath_in)
    corr_fft = np.fft.fft(corr)
    plot_arr = np.square(np.absolute(corr_fft))
    plt.figure(2)
    plt.plot(time, plot_arr)
    plt.ylim(-5, 100)  # Due to high value at zero
    plt.savefig(filepath_out+"autocorr_fft_plot.pdf")
    plt.show()

    return
>>>>>>> origin/ben
