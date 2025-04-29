import random

def main(num1,num2):
    if num1 < num2:
        print(random.choice([i for i in range(num1, num2+1) if i % 2 == 0]))

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
main(start,end)