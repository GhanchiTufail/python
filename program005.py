# program005:

# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class StringClass:

    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter string : ")

    def print_string(self):
        print(self.string.upper())

    def test(self):
        print("test function")

string1 = StringClass()
string1.get_string()
string1.print_string()
string1.test()