'''Write a program that takes cost price and selling price as input and displays whether the transaction is a
Profit or a Loss or Neither.
INPUT FORMAT
The first line contains the cost price.
The second line contains the selling price.
OUTPUT FORMAT
Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither
profit nor loss, print "Neither". (You must not have quotes in your output)
NOTE:
Please stick to the input and output format. Don't add anything extra like
'Enter cost price', 'Enter selling price', etc'''
cost_price=int(input())
selling_price=int(input())
if(cost_price>selling_price):
    print("Loss")
elif(cost_price<selling_price):
    print("Profit")
else:
    print("Neither")
