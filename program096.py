# program 96:

# Please write a program which count and print the numbers of each
# character in a string input by console.

# Example:
# If the following string is given as input to the program:

sentence = input("Enter the sentence : ")
print(sentence)

alphs = {}

for i in sentence:
    alphs[i] = sentence.count(i)

print(alphs)