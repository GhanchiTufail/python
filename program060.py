import re

def main(string):
    mylist = re.split("[ ,]",string)
    temp = []
    for i in mylist:
        if i.isdigit():
            temp.append(i)
    return temp

string = input("Enter the string : ")
print(main(string))