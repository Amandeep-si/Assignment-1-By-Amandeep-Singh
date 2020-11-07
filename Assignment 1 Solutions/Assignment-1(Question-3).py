'''Write a program that takes cost price and selling price as input and displays whether the transaction is a
Profit or a Loss or Neither.'''
cp=int(input("Enter your cost price: "))
sp=int(input("Enter your selling price: "))
if(cp>sp):
    print("Loss")
elif(cp<sp):
    print("Profit")
else:
    print("Neither loss nor profit")
