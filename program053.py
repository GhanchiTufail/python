# program 53 :

# Define a class named Rectangle which can be
# constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area_of_rectangle(self):
        print(self.width * self.length)
    
rect = Rectangle(int(input("Enter the length : ")),int(input("Enter the width : ")))
rect.area_of_rectangle()