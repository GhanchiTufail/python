# program 87:

# Please write a program to print the list after
# removing delete even numbers in [5,6,77,45,22,12,24].

# Hints:
# Use list comprehension to delete a bunch of element from a list.

mylist = [int(x) for x in input("Enter list : ").split(",") if int(x) % 2 == 0]
print(mylist)