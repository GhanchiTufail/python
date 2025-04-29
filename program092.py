# program 92:

# By using list comprehension, please write a program to print the list
# after removing the value 24 in [12,24,35,24,88,120,155].

# Hints:
# Use list's remove method to delete a value.

mylist = [int(x) for x in input("Enter the elements : ").split(",") if int(x) != 24]
print(mylist)