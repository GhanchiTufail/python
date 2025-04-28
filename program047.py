# program 47 :

# Write a program which can map() and filter() to make
# a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].


def main(start,end):
    lis = []
    for i in range(start,end+1):
        lis.append(i)
    
    map_func = map(lambda num : num ** 2,lis)
    filter_func = filter(lambda num : num ** 2,lis)
    print(list(map_func))
    print(list(filter_func))

start = int(input("Enter the start : "))
end = int(input("Enter the end : "))
main(start,end)