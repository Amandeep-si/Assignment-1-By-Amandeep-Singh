'''How to create a series from a numpy array?'''
import pandas as pd
import numpy as np
a1=np.array([10,42,63,49,25])
s1=pd.Series(a1)
print(s1)

