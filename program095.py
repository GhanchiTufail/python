# program 95:

# Define a class Person and its two child classes: Male and Female. All
# classes have a method "getGender" which can print "Male" for Male class
# and "Female" for Female class.

# Hints:
# Use Subclass(Parentclass) to define a child class.

class Person:
    def get_gender(self):
        print("Unknown")

class Male(Person):
    def get_gender(self):
        print("I am Male")

class Female(Person):
    def get_gender(self):
        print("I am Female")
        
ismale = Male()
isfemale = Female()

ismale.get_gender()
isfemale.get_gender()