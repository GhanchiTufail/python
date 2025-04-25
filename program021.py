# program 21 :

# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program
# to compute the distance from current position after a sequence
# of movement and original point. If the distance
# is a float, then just print the nearest integer.

# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

from math import sqrt

def main():
    y = 0
    x = 0
    while True:
        string = input("Enter the movement : ")
        if not string:
            break
        mylist = string.split(" ")
        if mylist[0] == "UP":
            y += int(mylist[1])
        if mylist[0] == "DOWN":
            y -= int(mylist[1])
        if mylist[0] == "RIGHT":
            x += int(mylist[1])
        if mylist[0] == "LEFT":
            x -= int(mylist[1])
        else:
            pass
    return round(sqrt((x*x) + (y*y)))

if __name__ == "__main__":
    print(main())