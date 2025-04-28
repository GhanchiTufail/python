# program 42 :

# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values
# in one line and the last half values in one line.

def main(start, end):
    tup = []
    for i in range(start,end+1):
        tup.append(i)
    tup = tuple(tup)
    half = len(tup) // 2  
    str1 = ""
    for i in range(start,half+1):
        if i != half:
            str1 = str1 + str(i) + ","
        else:
            str1 = str1 + str(i)
    print(str1)
    str1 = ""
    for i in range(half+1, end+1):
        if i != end:
            str1 = str1 + str(i) + ","
        else:
            str1 = str1 + str(i)
    print(str1)


start = int(input("Enter the number : "))
end = int(input("Enter the number : "))
main(start,end)