# program 34 :

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.


def main(number1,number2):
    dict1 = {}
    for i in range(number1,number2+1):
        dict1[i] = i**2
    return dict1


number1 = int(input("Enter the number : "))
number2 = int(input("Enter the number : "))
print(main(number1, number2))