import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ssc_course_team4.io_layer as io


def efield_fft(efield, thresh):
    """Process and plots the electric field data and its Fourier-transformed
    function.

    Args:
        efield (DataFrame): The DataFrame file (time, x, y, z columns).
        thresh (double integer): The threshhold value that the data should be
            checked against.

    Returns:
    """
#   Drop those exis below threshhold
    efield_df = pd.DataFrame(efield)
    efield_df = efield_df.drop(efield_df.var()
                               [efield_df.var() < thresh].index.values, axis=1)
#   Convert to numpy array for easier Fourier
    efield_np = efield_df.to_numpy()
    efield_np = efield_np.T
    efield_np_fft_data = np.fft.rfft(efield_np[1])
    efield_np_fft_freq = np.fft.rfftfreq(len(efield_np[0]))

    return efield_np_fft_data, efield_np_fft_freq


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

    dim2 = len(new_overlap[0])

    index_real = [x for x in range(0, dim2) if x % 2 == 0]
    index_complex = [x for x in range(0, dim2) if not x % 2 == 0]

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
