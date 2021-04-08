import numpy as np
import ssc_course_team4.statistical as st
import ssc_course_team4.io_layer as io
import filecmp
import os


def test_euclid_dis():
    """ Test Euclidean distance through statistical.euclid_dis()."""
    # Call function to test
    filepath = "ssc_course_team4/tests/data/ref_euclid_dis_data.dat"
    test_result = st.euclid_dis(io.read_in_np(filepath), 1e-5)

    # read in reference result
    filepath = "ssc_course_team4/tests/data/ref_euclid_dis_result.dat"
    ref_result = io.read_in_np(filepath)

    # compare both results
    assert np.allclose(test_result, ref_result, atol=1e-8)


def test_npop_corr():
    """ Test npop_corr through statistical.npop_corr().
    """

    # calling fuction to test with reference data
    filepath = "ssc_course_team4/tests/data/ref_npop_corr.csv"
    test_results = st.npop_corr(io.read_in_df(filepath), 1e-5)
    # print to file to compare it
    test_results.to_csv('testfile.csv')
    # reference results
    filepath = "ssc_course_team4/tests/data/ref_npop_corr_results.csv"

    # compare results
    assert filecmp.cmp('ssc_course_team4/tests/data/ref_npop_corr_results.csv',
                       'testfile.csv', shallow=True)
    # get rid of unnecessary amount of files
    os.remove('testfile.csv')
