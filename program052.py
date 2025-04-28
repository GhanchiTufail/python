# program 52 :

# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

class Circle():
    def __init__(self,radius):
        self.radius = radius
    
    def area_of_circle(self):
        area = (22/7) * self.radius ** 2
        print("The area of circle is {}".format(area))
    
circle1 = Circle(20)
circle1.area_of_circle()