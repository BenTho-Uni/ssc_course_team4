import sys
import os
import numpy as np
sys.path.insert(0, '../')
import src.ssc_course_team4.numerical as num


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
    np.savetxt("numerical_corr_test.t", array_to_export, delimiter=" ", header="necessary header")
    return array_to_export

def ref_out(time_dim, wfn_dim):
    time = time_arr(time_dim)
    corr_out = np.ones(time_dim)*wfn_dim*2 + 1j * np.zeros(time_dim)
    return time, corr_out



def test_autocorr():
    """test for the function, which generates the autocorrelation- and time array"""
    time_dim = 3
    wfn_dim = 3
    build_file_for_autocorr(time_dim, wfn_dim)
    time, corr = num.autocorr("numerical_corr_test.t")
    time_ref, corr_ref = ref_out(time_dim, wfn_dim)
    assert all([a == b for a,b in zip(time, time_ref)])
    assert all([a == b for a,b in zip(corr, corr_ref)])
    #assert num.autocorr("numerical_corr_test.t").all == ref_out(time_dim, wfn_dim).all

    os.remove("numerical_corr_test.t")
