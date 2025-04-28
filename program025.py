# program 25 :

# Define a class, which have a class parameter and have a same instance
# parameter.

class Person:

    def __init__(self, name):
        self.name = name

    def info(self):
        print("Name of the person is : {}".format(self.name))
    
name1 = Person(input("Enter first person's name : "))
print(name1.info)
print(name1.info())