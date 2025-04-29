# program 99:

# Please write a program which prints all permutations of [1,2,3]

# Hints:
# Use itertools.permutations() to get permutations of list.

import itertools

def main(mylist):
    print(list(itertools.permutations(mylist)))

data = [int(x) for x in input("Enter the elements : ").split(",")]
result = main(data)
result