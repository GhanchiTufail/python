#!/usr/bin/python
# -*- coding: utf-8 -*-

# program001 :

# Define the program name
# Write a program which will find all such numbers which are
# divisible by 7 but are not a multiple of 5, between 2000
# and 3200 (both included).

# The numbers obtained should be printed in a comma-separated
# sequence on a single line.

# Hints:
# Consider use range(#begin, #end) method

# all logic should be in side main method only


def main(start, end): #created main function
    mylist = []  # created empty list
    for i in range(start, end): # started for loop for the given start and end
        if i % 7 == 0 and i % 5 != 0: # logic for the output
            mylist.append(str(i)) # append the data to list in string form
    return ",".join(i for i in mylist) # converting list in to comma seprated values

if __name__ == "__main__":
    try:
        start = int(input("Enter first number : "))
        end = int(input("Enter last number : "))
        print("The out put is {}".format(main(start,end+1)))
    except:
        print("CHECK INPUT")