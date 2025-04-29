# program 77:

# Please write a program to output a random number,
# which is divisible by 5 and 7, between 0 and 10
# inclusive using random module and list comprehension.

# Hints:
# Use random.choice() to a random element from a list.


import random

def main(num1,num2):
    if num1 < num2:
        mylist = []
        for i in range(num1,num2+1):
            if i % 5 == 0 and i % 7 == 0:
                mylist.append(i)
        print(random.choice(mylist))

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
main(start,end)