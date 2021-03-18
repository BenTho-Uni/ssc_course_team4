import numpy as np
import pandas as pd

def read_in_df(filedir, filename):
    name = '{}{}'.format(filedir, filename)
    print('Reading in file {} - pandas'.format(name))
    data = pd.read_csv(name, r'\s+')
    return data

def read_in_np(filedir, filname):
    name = '{}{}'.format(filedir, filename)
    print('Reading in file {} - numpy'.format(name))
    data = np.loadtxt(name, skiprows=1)
    #data = data.T
    return data
