# program 41 :

# Define a function which can generate and print
# a tuple where the value are square of
# numbers between 1 and 20 (both included).

def main(num1, num2):
    tup = []
    for i in range(num1, num2+1):
        tup.append(i**2)
    return tuple(tup)

num1 = int(input("Enter the starting number : "))
num2 = int(input("Enter the ending number : "))
print(main(num1,num2)) 