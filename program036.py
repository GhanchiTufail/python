# program 36 :

# Define a function which can generate a dictionary
# where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the
# keys only.


def main(number1,number2):
    dict1 = {}
    for i in range(number1,number2+1):
        dict1[i] = i**2
    for i in dict1.keys():
        print(i)

if __name__ == "__main__":
    number1 = int(input("Enter the number : "))
    number2 = int(input("Enter the number : "))
    main(number1, number2)