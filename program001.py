# program001 :

# Define the program name
# Write a program which will find all such numbers which are
# divisible by 7 but are not a multiple of 5, between 2000
# and 3200 (both included).

# The numbers obtained should be printed in a comma-separated
# sequence on a single line.



def main(start, end):
    mylist = [] 
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            mylist.append(str(i))
    return ",".join(i for i in mylist)


start = int(input("Enter first number : "))
end = int(input("Enter last number : "))
print("The out put is {}".format(main(start,end+1)))
print("CHECK INPUT")