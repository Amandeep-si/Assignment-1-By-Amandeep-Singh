'''Accept two lists of 5 elements each from the user.
Convert them to numpy arrays. Concatenate these arrays and print it. Also sort these arrays and print it.
'''
import numpy as np
list1=[]
print("Enter your 5 numbers in your 1st list:")
for i in range(5):
    n=int(input())
    list1.append(n)
a=np.array(list1)
list2=[]
print("Enter your 5 elements in your 2nd list:")
for i in range(5):
    m=int(input())
    list2.append(m)
b=np.array(list2)
c=np.concatenate([a, b])
print("After Concatination:\n",c)
d=np.sort(c)
print("Your sorted array:\n",d)


