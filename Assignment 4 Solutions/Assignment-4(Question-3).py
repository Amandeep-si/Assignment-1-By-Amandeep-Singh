'''How to convert the index of a series into a column of a dataframe?'''
import pandas as pd
import numpy as np
a1=np.array([10,42,63,49,25])
s1=pd.Series(a1)
df = s1.to_frame().reset_index()
print(df)


