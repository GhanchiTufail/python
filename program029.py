# program 29 :

# Define a function that can receive
# two integral numbers in string form
# and compute their sum and then print it in console.

def main(num1,num2):
    return int(num1) + int(num2)

if __name__ == "__main__":
    num1 = input("Enter the number : ")
    num2 = input("Enter the number : ")
    print(main(num1, num2))