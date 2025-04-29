# program 75:

# Please generate a random float where the
# value is between 10 and 100 using Python math module.

# Hints:
# Use random.random() to generate a random float in [0,1].

import random

def main(start,end):
    if start > end:
        return "The starting value must be greater than end"
    num = random.uniform(start,end+1)
    return num

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
result = main(start,end)
print(result)