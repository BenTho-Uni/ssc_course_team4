import pytest
import numpy as np
import pandas as pd
import math
import sys
sys.path.insert(0, '..')
import src.ssc_course_team4.numerical as nm
import src.ssc_course_team4.io_layer as io

def test_efield_fft():
    """Test Function for numerical.efield_fft(), checks sinus wave function
    against reference file in /data."""
    # generate sinus function along y axis
    array_time = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    array_x = np.zeros(11)
    array_y = np.zeros(11)
    array_z = np.zeros(11)
    for i in range(0, 11):
        array_y[i] = math.sin(2*array_time[i]*np.pi)

    # create DataFrame from these arrays
    test_df = pd.DataFrame(np.array([array_time, array_x, array_y, array_z]).transpose(),
            columns=['time', 'x', 'y', 'z'])

    # load reference from file
    ref_data = np.loadtxt("data/efield_fft_data_ref.csv", dtype=np.complex_)
    ref_freq = np.loadtxt("data/efield_fft_freq_ref.csv")

    # test function to generate data
    test_data, test_freq = nm.efield_fft(test_df, 1e-5)

    #compare arrays
    assert np.array_equal(test_data, ref_data)
    assert np.array_equal(test_freq, ref_freq)
