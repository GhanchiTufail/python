# program009 :
# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the

# program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def main(sentence):
    return sentence.upper()

if __name__ == "__main__":
    sentence = input("Enter sentence : ")
    print(main(sentence))