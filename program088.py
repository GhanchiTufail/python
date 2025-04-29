# program 88:

# By using list comprehension, please write a program
# to print the list after removing delete numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

mylist = [int(x) for x in input("Enter elements : ").split(",") if int(x) % 7 == 0 and int(x) % 5 == 0]
print(mylist)