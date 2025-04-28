# program 15 :

# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106


def main(data):
    k = data
    k1 = k + (data * 10)
    k2 = k1 + (data * 100)
    k3 = k2 + (data * 1000)
    num = k + k1 + k2 + k3
    return num


data = int(input("Enter the number : "))
print(main(data))