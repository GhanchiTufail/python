# program 33 :

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.

def main(number):
    dict1 = {}
    for i in range(0,number+1):
        dict1[i] = i**i
    return dict1


number = int(input("Enter the number : "))
print(main(number))