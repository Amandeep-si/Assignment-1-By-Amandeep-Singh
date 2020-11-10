'''Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number.'''
l=[]
for i in range(0,10):
    n=int(input())
    if(n%2==0):
        l.append(n)
print(l)
