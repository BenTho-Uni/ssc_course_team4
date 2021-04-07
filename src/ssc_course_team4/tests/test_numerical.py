import numpy as np
import pandas as pd
import os
import ssc_course_team4.numerical as nm


def test_efield_fft():
    """Test Function for numerical.efield_fft(), checks sinus wave function
    against reference file in /data."""
    # generate sinus function along y axis
    array_time = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    array_x = np.zeros(11)
    array_y = np.zeros(11)
    array_z = np.zeros(11)
    for i in range(0, 11):
        array_y[i] = np.sin(2*array_time[i]*np.pi)

    # create DataFrame from these arrays
    test_df = pd.DataFrame(np.array([array_time, array_x, array_y,
                                    array_z]).transpose(),
                           columns=['time', 'x', 'y', 'z'])

    # load reference from file
    filepath = "ssc_course_team4/tests/data/efield_fft_data_ref.csv"
    ref_data = np.loadtxt(filepath,
                          dtype=complex)
    filepath = "ssc_course_team4/tests/data/efield_fft_freq_ref.csv"
    ref_freq = np.loadtxt(filepath)

    # test function to generate data
    test_data, test_freq = nm.efield_fft(test_df, 1e-5)

    # compare arrays
    # assert np.array_equal(test_data, ref_data)
    assert np.allclose(test_data, ref_data, atol=1e-08)
    # assert np.array_equal(test_freq, ref_freq)
    assert np.allclose(test_freq, ref_freq, atol=1e-08)


def time_arr(time_dim):
    time = []
    for val in np.arange(time_dim):
        time.append(np.float64(val))
    return np.array(time)


def autocorr_arr(time_dim, wfn_dim):
    autocorr = []
    for time_step in np.arange(time_dim):
        autocorr.append(np.ones(time_dim, dtype="complex"))
    autocorr_ = np.array(autocorr)
    autocorr_.imag[:] = 1
    return np.transpose(autocorr_)


def build_file_for_autocorr(time_dim, wfn_dim):
    autocorr_ = []
    time = time_arr(time_dim)
    for time_step in np.arange(time_dim):
        autocorr_.append(np.ones(time_dim*2))
    autocorr = np.array(autocorr_)
    array_to_export = np.insert(autocorr, 0, time, axis=1)
    np.savetxt("numerical_corr_test.t", array_to_export, delimiter=" ",
               header="necessary header")
    return array_to_export


def ref_out(time_dim, wfn_dim):
    time = time_arr(time_dim)
    corr_out = np.ones(time_dim)*wfn_dim*2 + 1j * np.zeros(time_dim)
    return time, corr_out


def test_autocorr():
    """test for the function,
    which generates the autocorrelation- and time array"""

    time_dim = 3
    wfn_dim = 3
    build_file_for_autocorr(time_dim, wfn_dim)
    time, corr = nm.autocorr("numerical_corr_test.t")
    time_ref, corr_ref = ref_out(time_dim, wfn_dim)
    assert all([a == b for a, b in zip(time, time_ref)])
    assert all([a == b for a, b in zip(corr, corr_ref)])

    # assert num.autocorr("numerical_corr_test.t").all == ref_out(time_dim,
    # fn_dim).all
    os.remove("numerical_corr_test.t")
