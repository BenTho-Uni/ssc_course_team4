import pytest
import numpy as np
import sys
sys.path.insert(0, '..')
import src.ssc_course_team4.numerical as nm

class build_efield:
    def __init__(self, npts, time_step, bx, by, bz):
        self.npts = npts
        self.time_step = time_step
        self.bx = bx
        self.by = by
        self.bz = bz

    def init_df(self):
        array_time = set()
        array_x = np.random.rand(self.npts) if self.bx else np.zeros(self.npts)
        array_y = np.random.rand(self.npts) if self.by else np.zeros(self.npts)
        array_z = np.random.rand(self.npts) if self.bz else np.zeros(self.npts)

        for i in self.npts:
            array_time.add(i*self.time_step)

        return pd.DataFrame(np.array([array_time, array_x, array_y, array_z]),
                            columns=['time', 'x', 'y', 'z'])

obj = build_efield(4, 0.1, False, True, False)
print (obj.init_df())
