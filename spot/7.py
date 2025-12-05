class Vehicle:
    _wheels = 4

    @classmethod
    def wheels(cls):
        return cls._wheels

print(Vehicle.wheels())

class Motorcycle(Vehicle):
    _wheels = 2

print(Motorcycle.wheels())
print(Vehicle.wheels())

class Car(Vehicle):
    pass

print(Vehicle.wheels())
print(Motorcycle.wheels())
print(Car.wheels())


'''
What does the code below output, and why? 
What does this demonstrate about class variables, and why we should avoid using class variables when working with inheritance?
'''

'''
Okay, so we have the first class that's been defined called Vehicle, which will help us figure out what line 8 would print. 

Within the class vehicle, we've got a class method which returns the value of a class variable called `_wheels`. And then we can see that the class variable has been defined in the body itself, which is for the first print statement. So, for now, let's move on to the next class definition, which is motorcycle.

Within motorcycle, we have a class variable defined called `wheels`, which has been assigned to the value of 2 and nothing more. So, line 13 calls. It's the calling class motorcycle, which calls the method `class_method` `wheels`. So, we know that there, we don't have a class method defined within motorcycle. So, we go up the inheritance list, which is a vehicle. And then, we find a class method `wheels` and the class here is motorcycle. So, what we'll do is we'll return motor site them. The class variable `wheels` that's been defined within motorcycle, so that value is going to be 2. So, the line 14 is still going to bring for as before.

Now, let's move on to the next class definition, which is car. Car also inherits from vehicle. To figure out what prints what will be printed on line 19, that is still going to be 4 because we're just calling the vehicle class on the class method `wheels`, which is 4. Motorcycle is going to be 2. So, that's just the same print statement as before. And then, in line 21, we would actually print 4 as well because there is no class variable or class method defined in car, so we go up the inheritance list and then we find that there is. A class variable that's been defined there. So, what this demonstrates about class variables is that they can be inherited and they follow the order of the method resolution order. We probably want to avoid using them because they can be quite hard to follow, and it'll be quite easy to make a mistake and does make the code slightly less predictable. 
'''