import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_in_df(filepath):
    print('Reading in file {} - pandas'.format(filepath))
    data = pd.read_csv(filepath, r'\s+')
    return data


def read_in_np(filepath):
    print('Reading in file {} - numpy'.format(filepath))
    data = np.loadtxt(filepath, skiprows=1)
    return data


def euclid_dis_plot(filepath_out, data):
    """Plots the Euclidean Distance as a plot of the different axis

    Args:
        filepath_out (string): The realtive output file filepath.
        data (numpy array): The data holding object.

    Returns:
        """
    plt.bar(range(0, len(data)), data)
    plt.savefig(filepath_out+'euclid_dis.pdf')
    return


def efield_plot(filepath_out, data):
    """Plots the electric field as a plot of the different axis

    Args:
        filepath_out (string): The realtive output file filepath.
        data (numpy array): The data holding object.

    Returns:
    """
    plt.plot(data['time'], data['x'])
    plt.plot(data['time'], data['y'])
    plt.plot(data['time'], data['z'])
    plt.savefig(filepath_out+'efield_plot.pdf')
    plt.close()
    return


def efield_fft_plot(filepath_out, data):
    """Plots the Fourier-transformed electric efield_df.

    Args:
        filepath_out (string): The realtive output file filepath.
        data (numpy array): The data holding object.
    Returns:"""
    efield_np_fft_data = np.fft.rfft(data[1])
    efield_np_fft_freq = np.fft.rfftfreq(len(data[0]))
    plt.plot(efield_np_fft_freq, abs(efield_np_fft_data**2))
    plt.savefig(filepath_out+'efield_fft.pdf')
    plt.close()
    return