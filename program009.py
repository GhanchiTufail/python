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


def main():
    mylist = []
    while True:
        data = input("Enter string : ")
        if data:
            mylist.append(data.capitalize())
        else:
            break
    for i in mylist:
        print(i)

if __name__ == "__main__":
    print()
    main()
    print()