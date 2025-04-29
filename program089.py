# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].

mylist = [int(x) for (index,x) in enumerate(input("Enter the list : ").split(",")) if index % 2 != 0]
print(mylist)