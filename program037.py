# program 37 :

# Define a function which can generate and print a list
# where the values are square of
# numbers between 1 and 20 (both included).

def main(num1, num2):
    list1 = []
    for i in range(num1, num2+1):
        list1.append(i**2)
    print(list1)



num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
main(num1,num2)