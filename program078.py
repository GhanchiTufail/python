
# program 78:

# Please write a program to generate a list
# with 5 random numbers between 100 and 200 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

import random

def main(start, end):
    print(random.sample(range(start,end),5))

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
main(0,10)