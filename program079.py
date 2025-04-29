
# program 79:

# Please write a program to randomly generate a list
# with 5 even numbers between 100 and 200 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

import random

def main(start, end):
    print(random.sample([x for x in range(start,end) if x % 5 == 0 and x % 7 == 0],5))

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
main(start,end)