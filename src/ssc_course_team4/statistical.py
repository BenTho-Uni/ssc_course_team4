import numpy as np
import pandas as pd
import io_layer


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
    efield = io_layer.read_in_df(filepath_in)
#   Plot efield per axis
    io_layer.efield_plot(filepath_out, efield)
#   Drop those exis below threshhold
    efield_df = pd.DataFrame(efield)
    efield_df = efield_df.drop(efield_df.var()
        [efield_df.var() < thresh].index.values, axis=1)
#   Convert to numpy array for easier Fourier
    efield_np = efield_df.to_numpy()
    efield_np = efield_np.T
#   Plot fft
    io_layer.efield_fft_plot(filepath_out, efield_np)
    return
