# program 65:

# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# with a given n input by console (n>0).

def main(num):
    if num == 0:
        return 0
    else:
        return main(num-1) + (100) 


num = int(input("Enter input : "))
print(main(num))