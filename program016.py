# program 16 :

# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9


def main(mylist):
    list1 = []
    for i in mylist:
        if int(i) % 2 != 0:
            list1.append(i)
    return list1

if __name__ == "__main__":
    try:
        string = input("enter the number : ")
        mylist = string.split(",")
        print(main(mylist))
    except:
        ValueError("Check Value")