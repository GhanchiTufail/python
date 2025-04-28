# program 43 :

# Write a program to generate and print another
# tuple whose values are even numbers
# in the given tuple (1,2,3,4,5,6,7,8,9,10).

def main(start, end):
    temp = []
    for i in range(start,end+1):
        temp.append(i)
    tup = tuple(temp)
    temp = []
    for i in tup:
        if i%2 == 0:
            temp.append(i)
    even_tuple = tuple(temp)
    print(even_tuple)

start = int(input("Enter the start : "))
end = int(input("Enter the end : "))
main(start,end)
