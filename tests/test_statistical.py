import pytest
import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '..')
import src.ssc_course_team4.statistical as st
import src.ssc_course_team4.io_layer as io


def test_euclid_dis ():
    """ Test Euclidean distance through statistical.euclid_dis()."""
    # Call function to test
    test_result = st.euclid_dis(io.read_in_np("data/ref_euclid_dis_data.dat"), 1e-5)

    # read in reference result
    ref_result = io.read_in_np("data/ref_euclid_dis_result.dat")

    # compare both results
    assert np.array_equal(test_result, ref_result)
