# program 93:

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the
# above given lists.

# Hints:
# Use set() and "&=" to do set intersection operation.

set1 = set(input("Enter the elements : ").split(","))
set2 = set(input("Enter the elements : ").split(","))
 
set1 &= set2
mylist = set1

print(mylist)