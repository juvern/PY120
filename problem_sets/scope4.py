'''
Create a Car class that has a class variable named manufacturer and an instance variable named manufacturer. Initialize these variables to different values. Add a show_manufacturer method that prints both the class and instance variables.
'''

class Car:
    manufacturer = "Ford"

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f"The class instance is {self.__class__.manufacturer}")
        print(f"The self instance is {self.manufacturer}")


tesla = Car('Tesla')
tesla.show_manufacturer()

