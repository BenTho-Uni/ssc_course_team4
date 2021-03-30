import pytest
import numpy as np
import pandas as pd
import sys
sys.path.insert(0, '..')
import statistical as sl

#import sys
#sys.path.insert(0, '..')
#import src.ssc_course_team4.io_layer as io

#original_df = io.read_in_df('../data/npop.t')


#class build_df:
#    def __init__(self, npts):
#        self.npts = npts
#        # array_time = np.zeros(self.npts)
#        array_time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#        array_x = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1]
#        array_y = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1]
#        array_z = np.zeros(self.npts)
#
#        return pd.DataFrame(np.array([array_time, array_x, array_y, array_z]).transpose(),
#        columns=['time', 'x', 'y', 'z'])

class build_df:
    def __init__(self, name):
        self.dfnamepath = name

    def read_df(self):
        self.data = pd.read_csv(self.dfnamepath, r'\s+')
        return self.data


@pytest.fixture
#def test_df_npop():
#    obj = build_df(10)
#    return obj.init_df()


# print(test_df_npop())
def get_df():
    obj = build_df('./tests/test_df_nils.csv')
    data = obj.read_df()
    return data

threshv = 0


def test_npop_corr(get_df):
    corrmat = sl.npop_corr(, 'get_df.out',threshv)
    corrmat = corrmat.dropna().round(decimals=6)
    d = [0.832628, 0.228204, 0.136257]
    ind = pd.MultiIndex.from_tuples([
                                   ('norm', '<H>'),
                                   ('<z>', '<H>'),
                                   ('norm', '<z>')])
    ser_new = pd.Series(data=d, index=ind)
    assert corrmat.equals(ser_new)


#def npop_corr(inserted_df, threshv):
#    df_npop = inserted_df
#    # print(df_npop.columns)
#                df_npop.var()[df_npop.var() < threshv].index.values, axis=1)
#    value_list = set()
#    column_names = df_npop2_short.columns
#    for i in range(0, df_npop2_short.shape[1]):
#        for j in range(0, i+1):
#            value_list.add((column_names[i], column_names[j]))
#    final_correlation = df_npop2_short.corr().unstack()
#    final_correlation = final_correlation.drop(labels=value_list).sort_values(
#                                ascending=False, key=lambda col: col.abs())
#    with open(filepath_out+'npop_corr.cvs', 'w') as f:
#        print(final_correlation, file=f)
#    return final_correlation

#print(npop_corr(original_df, 0.00001))
#print(npop_corr(test_df_npop, 0.00001))

#def test_npop_corr():
#    """ test function to test calc of correlation calculation
#    """
#    assert npop_corr(test_df)
#function für input
#insert function in pytest
#    input in function
#    assert function um ergebnis fct call für vgl zu
