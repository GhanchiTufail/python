# program 80:

# Please write a program to randomly generate a
# list with5 numbers, which are divisible by 5 and 7 ,
# between 1 and 1000 inclusive.


import random

def main(start, end):
    print(random.sample([x for x in range(start,end) if x % 5 == 0 and x % 7 == 0],5))

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
main(start,end)