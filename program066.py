# program 66:

# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value
# of f(n) with a given n input by console.

def main(num):
    x = 0
    y = 1
    temp = 0
    for i in range(0,num):
        temp = x + y
        x = y
        y = temp
    return temp
        
data = int(input("Enter the number : "))
print(main(data))