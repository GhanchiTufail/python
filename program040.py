# program 40 :

# Define a function which can generate a list
# where the values are square of
# numbers between 1 and 20 (both included).
# Then the function needs to print all values
# except the first 5 elements in the list.

def main(num1, num2):
    list1 = []
    for i in range(num1, num2):
        list1.append(i**2)
    k = 0
    for i in list1:
        if k < 5:
            k+=1
            continue
        else:
            print(i)


num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
main(num1,num2)