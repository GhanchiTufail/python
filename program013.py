# program 13 :

# Write a program that accepts a sentence and
# calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


def main(string):
    digits = 0
    characters = 0
    for i in string:
        if i.isdigit():
            digits += 1
        if i.isalpha():
            characters += 1
    return {
        "Digits":digits,
        "Alphabets":characters
    }


string = input("Enter the sentence : ")
print(main(string))