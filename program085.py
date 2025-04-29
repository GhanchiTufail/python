
# program 85:

# Please write a program to shuffle
# and print the list [3,6,7,8].

# Hints:
# Use shuffle() function to shuffle a list.

import random

def main(mylist):
    random.shuffle(mylist)

def string_to_list(string):
    mylist = string.split(",")
    int_list = [int(x) for x in mylist]
    return int_list

string = input("Enter the string : ")
mylist = string_to_list(string)
print(mylist)
result = main(mylist)
print(mylist)