# program 39 :

# Define a function which can generate a list
# where the values are square of
# numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.


def main(num1, num2):
    list1 = []
    temp = []
    for i in range(num1, num2+1):
        list1.append(i**2)
    for i in range(len(list1), len(list1)-6, -1):
        temp.append(i)
    temp.reverse()
    print(temp)

num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
main(num1,num2)