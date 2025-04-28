# program 46 :

# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

def is_even(num):
    return num ** 2

def main(start, end):
    lis = []
    for i in range(start,end+1):
        lis.append(i)

    print(list(map(is_even,lis)))

start = int(input("Enter the start : "))
end = int(input("Enter the end : "))
main(start,end)