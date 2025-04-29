# program 72:

# Please write a binary search function which
# searches an item in a sorted list.
# The function should return
# the index of element to be searched in the list.

# Hints:
# Use if/elif to deal with conditions.


def string_to_list(senternce):
    mystr = senternce.split(",")
    mylist = [int(x) for x in mystr]
    return unique_sorted_elements(mylist)


def unique_sorted_elements(mylist):
    return sorted(list(set(mylist)))


def binary_search(element,mylist):
    mylist = string_to_list(mylist)
    beg = 0
    end = len(mylist) - 1

    while beg <= end:
        mid = (beg + end) // 2

        if element > mylist[mid]:
            beg = mid + 1
        elif element < mylist[mid]:
            end = mid - 1 
        else:
            return f"Element {element} is at index {mid}"
    return f"Element does not exist"


mylist = input("Enter the number in coma seprated : ")
element = int(input("Enter the input : "))
print(binary_search(element,mylist))