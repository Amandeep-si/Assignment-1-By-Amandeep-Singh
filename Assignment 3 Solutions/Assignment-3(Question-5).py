'''Consider two square numpy arrays. Stack them vertically and horizontally.'''
import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print("Vertical stacking:\n", np.vstack((a, b)))
print("\nHorizontal stacking:\n", np.hstack((a, b)))
