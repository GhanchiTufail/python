# program 45 :

# Write a program which can filter even numbers in
# a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

def main(start,end):
    list1 = []
    for i in range(start,end+1):
        list1.append(i)

    filtered = filter(lambda num: num % 2 == 0, list1)
    for i in filtered:
        print(i)

start = int(input("Enter the start : "))
end = int(input("Enter the end : "))
main(start,end)
