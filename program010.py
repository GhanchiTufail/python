# program010 :

# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

# Suppose the following input is supplied to the
# program:
# hello world and practice makes perfect and hello world again

# Then, the output should be:
# again and hello makes perfect practice world


import logging

def main(sentence):
    mylist = sentence.split(" ")
    mylist = list(set(mylist))
    mylist.sort()
    data = " ".join(mylist)
    return data

if __name__ == "__main__":
    try:
        sentence = input("Enter the sentence : ")
        print(main(sentence))
    except:
        logging.warning("Value error")