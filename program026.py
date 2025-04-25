# program 26 :

# Define a function which can compute the sum of two numbers.

def main(num1, num2):
    return num1 + num2

if __name__ == "__main__":
        try:
              print("The total is : " , main(int(input("Enter a number : ")),int(input("Enter a number : "))))
        except:
              print("Check Value")