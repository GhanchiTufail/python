# program 12 :

# Write a program, which will find all such numbers
# between 1000 and 3000 (both included) such
# that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on
# a single line.


def main(start,end):
    mylist = []

    while start <= end :
        if start % 2 == 0:
            ans = True
            temp = start
            while ans == True:
                k = temp % 10
                temp = temp // 10
                if k % 2 != 0:
                    ans = False
                    break    
                if temp == 0:
                    break
            if ans == True:
                mylist.append(start)
        start += 1
    return mylist


if __name__ == "__main__":
    try:
        start = int(input("Enter the start value : "))
        end = int(input("Enter the end value : "))
        print(main(start,end))
    except:
        ValueError("Enter the integer")