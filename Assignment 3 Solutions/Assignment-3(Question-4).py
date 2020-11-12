'''How to convert a 1D array into a 2D array? Demonstrate with the help of a code snippet
Hint: np.newaxis, np.expand_dims'''
import numpy as np
print("****** Converting 1-D array into 2D array******")
print()
#we can use np.newaxis to increase the dimension of one of the arrays so that NumPy can broadcast.
print("---By using 'np.newaxis' Method---\n")
# 1D array
arr = np.arange(4)
print(arr)
print("Shape of the Array: ",arr.shape)
# make it as row vector by inserting an axis along first dimension
row_vec = arr[np.newaxis, :]     # arr[None, :]
print("Row Vector:")
print("Shape of the array: ",row_vec.shape)
# make it as column vector by inserting an axis along second dimension
col_vec = arr[:, np.newaxis]     # arr[:, None]
print("Column Vector:")
print("Shape of the array: ",col_vec.shape)
print()
#There is another very similar functionality in NumPy: np.expand_dims, which can also be used to insert one dimension:
print("---By Using 'np.expand_dims' Method---\n")
a = np.arange(10)
print(a)
print(np.expand_dims(a, 1))  # like a[:, np.newaxis]
print(np.expand_dims(a, 0))
print()
print("---By Using 'reshape' Method---")
x1 = np.arange(1,10)
print(x1)
print(x1.shape)
print("Dimension: ",x1.ndim)
x1=np.arange(1,10).reshape(3,3)
print(x1)
print(x1.shape)
print("Dimension: ",x1.ndim)

