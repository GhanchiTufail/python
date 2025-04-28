# program 56 :

# Write a function to compute 5/0 and use try/except to catch the exceptions.

try:
    Dividend = int(input("Enter the dividend : "))
    Divisor = int(input("Enter the divisor : "))
    print(Dividend/Divisor)
except ZeroDivisionError:
    print("Division by zero is not allowed")