'''Write a program to compute the distance between the current position after
a sequence of movement and original point. If the distance is a float, then
just print the nearest integer (use round() function for that and then convert
it into an integer).'''
pos = {"x":0,"y":0}
n = int(input("Input\n"))
for i in range (n):
    move = input().split(" ")
    if move[0].lower() == "up":
        pos["y"] += int(move[1])
    elif move[0].lower() == "down":
        pos["y"] -= int(move[1])
    elif move[0].lower() == "left":
        pos["x"] -= int(move[1])
    elif move[0].lower() == "right":
        pos["x"] += int(move[1])
print("Output\n",int(round((pos["x"]**2 + pos["y"]**2)**0.5)))