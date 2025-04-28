# program 44 :

# Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

def main(string):
    if string.lower() == "yes":
        print("Yes")
    else:
        print("No")

string = input("Enter the string : ")
main(string)