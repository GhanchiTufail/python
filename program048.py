# program 48 :

# Write a program which can filter() to make a list
# whose elements are even number between 1 and 20 (both included).

def main(start, end):
    mylist = []
    for i in range(start, end+1):
        mylist.append(i)
    even = filter(lambda num : num % 2 == 0, mylist)

    print(list(even))

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending value : "))
main(start,end)