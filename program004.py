# program004:

# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


from logging import warning

def string_append(string, data, i):
    if i == 0:
        string = data
    else:
        string = string + "," + data
    return string


def main(limit):
    string = ""
    for i in range(0,limit):
        data = (input("Enter number : "))
        string = string_append(string, data, i)
    mylist = string.split(",")
    mytuple = tuple(mylist)
    return {
            "list":mylist,
            "tuple":mytuple
            }


if __name__ == "__main__":
    try:
        limit = int(input("Enter the data range : "))
        data = main(limit)
        print("The list is : {}".format(data["list"]))
        print("The tuple is : {}".format(data["tuple"]))
    except:
        warning("check value")