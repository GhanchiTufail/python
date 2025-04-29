# program 69:

# Please write a program using generator to print
# the numbers which can be divisible by 5 and 7
# between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 100

# Then, the output of the program should be:

# 0,35,70


def main(num):
    mylist = []
    for i in range(1,num+1):
        if i % 5 == 0 and i % 7 == 0:
            mylist.append(str(i))
    return ",".join(mylist)

data = int(input("Enter the number : "))
print(main(data))