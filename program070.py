def main(data):
    for i in data:
        assert int(i) % 2 == 0

try:
    string = input("Enter the number in coma seprated value : ")
    mylist = string.split(",")
    main(mylist)
except AssertionError:
    print("all numbers are not even")