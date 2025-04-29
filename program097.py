# program 97:

# Please write a program which accepts a string from console and print it
# in reverse order.

# Example:
# If the following string is given as input to the program:

# rise to vote sir

# Then, the output of the program should be:

# ris etov ot esir

# Hints:
# Use list[::-1] to iterate a list in a reverse order.

def main(string):
    mylist = []
    for i in string:
        mylist.append(i)
    mylist.reverse()
    mystr = "".join(mylist)
    print(mystr)

string = input("Enter the string : ")