'''Write a code snippet to find the dimensions of a ndarray and its size.'''
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(arr)
print("No. of dimensions of the given array is: ", arr.ndim)
print("Size of given array is: ", arr.size)