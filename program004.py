# program004:

# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


def main(string: str):
    list1 = []
    list1 = string.split(",")
    tup = tuple(list1)
    return list1,tup

if __name__ == "__main__":
    limit = (input("Enter the data range : "))
    data = main(limit)
    print("The list is : {}".format(data[0]))
    print("The list is : {}".format(data[1]))