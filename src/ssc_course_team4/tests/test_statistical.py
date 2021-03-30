import numpy as np
import ssc_course_team4.statistical as st
import ssc_course_team4.io_layer as io


def test_euclid_dis():
    """ Test Euclidean distance through statistical.euclid_dis()."""
    # Call function to test
    filepath = "ssc_course_team4/tests/data/ref_euclid_dis_data.dat"
    test_result = st.euclid_dis(io.read_in_np(filepath), 1e-5)

    # read in reference result
    filepath = "ssc_course_team4/tests/data/ref_euclid_dis_result.dat"
    ref_result = io.read_in_np(filepath)

    # compare both results
    assert np.array_equal(test_result, ref_result)
