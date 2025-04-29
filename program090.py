# program 90:

# By using list comprehension, please write a program generate a 3*5*8 3D
# array whose each element is 0.

# Hints:
# Use list comprehension to make an array.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

my_list = [[['0' for i in range(c)] for j in range(b)] for k in range(a)]
print(my_list)