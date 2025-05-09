# program 17 :

# Write a program that computes the net amount of
# a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500


def main():
    amount = 0
    while True:
        data = input()
        if not data:
            break
        operation = data[0]
        value = int(data[1:])
        if operation == "D":
            amount += value
        if operation == "W":
            if value > amount:
                print("Less balance")
            else:
                amount -= value
        else:
            pass
    return "Total balance is : {}".format(amount)

print(main())