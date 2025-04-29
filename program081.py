# program 81:

# Please write a program to randomly print
# an integer number between 7 and 15 inclusive.

import random

def main(num1,num2):
    return random.randrange(num1,num2)

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
print(main(start,end))