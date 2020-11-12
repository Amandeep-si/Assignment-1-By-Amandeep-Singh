'''How to get unique items and counts of unique items?'''
import numpy as np
arr = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18])
print('Original Numpy Array:\n ', arr)
uniqueValues, occurCount = np.unique(arr, return_counts=True)
print('Unique Values :\n ',uniqueValues)
print("Occurrence Count :\n ", occurCount)
print('Unique Values along with occurrence Count')
listOfUniqueValues = zip(uniqueValues, occurCount)
for elem in listOfUniqueValues:
   print(elem[0] , ' Occurs : ' , elem[1], ' times')
