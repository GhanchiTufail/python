# program 30 :

# Define a function that can accept two strings
# as input and concatenate them and then print it in console.


def main(str1, str2):
    return str1 +" "+ str2

if __name__ == "__main__":
    str1 = input("Enter the string : ")
    str2 = input("Enter the string : ")
    print(main(str1,str2))