# program 49 :

# Write a program which can map() to make a list whose
# elements are square of numbers between 1 and 20 (both included).

def main(start, end):
    mylist = []
    for i in range(start,end+1):
        mylist.append(i)
    
    square = map(lambda num : num ** 2 , mylist)
    print(list(square))

start = int(input("Enter the first value : "))
end = int(input("Enter the last value : "))
main(start,end)