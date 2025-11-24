'''
Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided at instantiation time.

You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.

Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.

Create a method that prints a message about the car's current speed.
Write some code to test the methods.

Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. 

You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests.
'''

class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color # triggers setter because @color.setter
        self.speed = 0

    @property
    def color(self):
        return self._color

    @color.setter
    # Because it has a setter, Python calls that setter method instead of directly setting an attribute
    def color(self, color):
        self._color = color # where the actual value lives

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year


    def engine_on(self):
        print(f"{self.model} - Engine on")

    def accelerate(self):
        self.speed += 10
        print(f"{self.model} - Accelerate")

    def brake(self):
        self.speed -= 10
        print(f"{self.model} - Brake")

    def engine_off(self):
        print(f"{self.model} - Engine off")

    def get_speed(self):
        print(f"{self.model}'s speed is at {self.speed}")

    def spray_paint(self, color):
        self.color = color  # this invokes the @color.setter

    @classmethod
    def avg_gas_mileage(cls, distance, fuel):
        print(f"The average gas mileage is {distance / fuel}")


martin = Car("Ford Fiesta", 2006, "red") # class constructor

martin.engine_on()
martin.accelerate()
martin.accelerate()
martin.accelerate()
martin.brake()

martin.get_speed()

print(martin.color)
martin.color = "blue"
print(martin.color)
martin.spray_paint("yellow")
print(martin.avg_gas_mileage(1000, 30))
martin.year = 2020 # return AttributeError
martin.model = "Tesla" # return AttributeError
