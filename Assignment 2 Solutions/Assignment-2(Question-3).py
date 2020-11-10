'''In this assignment, given a number n, you have to write a program that generates a dictionary d which
contains (i, i*i), where i is from 1 to n (both included).'''
n=int(input("Input:\n"))
dict1=dict()
for i in range(1,n+1):
    dict1[i]=i*i
print("Output:\n",dict1)