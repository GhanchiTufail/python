# program006:

# Write a program that calculates and prints the value according to the
# given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a
# comma-separated sequence.

# Example
# Let us assume the following comma separated input sequence
# is given to the program:
# 100,150,180

# The output of the program should be:
# 18,22,24


from math import sqrt

print(round(20.8))

def main(data: str):
    C = 50
    H = 30

    value = []
    num = [i for i in data.split(",")]
    for i in num:
        value.append(str(int(round(sqrt(2 * C * float(i)/H)))))
    return value
if __name__ == "__main__":
    data = input("Enter input : ")
    print(main(data))