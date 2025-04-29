# program 67:

# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program using list comprehension
# to print the Fibonacci Sequence
# in comma separated form with a given n input by console.

# Example:
# If the following n is given as input to the program:

# 7

# Then, the output of the program should be:

# 0,1,1,2,3,5,8,13


def main(num):
    x = 0
    y = 1
    temp = 0
    string = "0,1,"
    for i in range(0,num):
        temp = x + y
        x = y
        y = temp
        if i+1 == num:
            string = string + str(temp)
        else:
            string = string + str(temp) + ","
        string = string + ""
    return string
        
data = int(input("Enter the number : "))
print(main(data))