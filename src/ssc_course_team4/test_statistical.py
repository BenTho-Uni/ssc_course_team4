import unittest
import os
import filecmp
import io
import statistical as st  # Find out how to do this inside test folder


class test_npop_corr (unittest.TestCase):
    def test_npop_corr(self):
        # prepare fielpaths to input and reference
        filepath_in = os.path.join('..', '..', 'data', 'npop.t')
        filepath_ref = os.path.join('tests', 'data', 'ref_npop_corr.cvs')

        # run function to test
        st.npop_corr(filepath_in, "", 1e-05)

        # check if both files are the same
        # ToDo: why below check not working? If works, how to delete after fail
        # self.assertTrue(filecmp.cmp(filepath_in, filepath_ref, True), "The output file differs from reference.")
        self.assertListEqual(list(io.open('npop_corr.cvs')),
                            list(io.open(filepath_ref)))

        # clean up
        os.remove('npop_corr.cvs')
        return
