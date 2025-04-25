# program002 :

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


def main(number):
    if number == 1:
        return 1
    return number * main(number-1)
    # count = 1
    # while number > 1:
    #     count = count * number
    #     number -= 1
    # return count
    
if __name__ == "__main__":
    try:
        number = int(input("Enter the number : "))
        print("The factorial of the number {0} is : {1}".format(number , main(number)))
    except:
        print("check value")