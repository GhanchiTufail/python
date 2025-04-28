# program 51 :

# Define a class named American and its subclass NewYorker.

class America:
    def Country(self):
        print("This is America country")
    
class NewYorker(America):
    def City(self):
        print("This is New York City")

city = NewYorker()
city.Country()
city.City()