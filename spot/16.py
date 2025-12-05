class Wheel:
    def __init__(self):
        self.is_flat = False

    def go_flat(self):
        self.is_flat = True

class Car:
    def __init__(self, name, front_wheel, back_wheel):
        self.name = name
        self.front_wheel = front_wheel # A Wheel collaborator
        self.back_wheel = back_wheel   # A Wheel collaborator

    def drive_over_nail(self):
        # A nail only punctures the front wheel
        self.front_wheel.go_flat()

    def get_wheel_statuses(self):
        return (f"Front wheel is_flat: {self.front_wheel.is_flat}\n"
                f"Back wheel is_flat: {self.back_wheel.is_flat}")

# Setup
common_wheel = Wheel()
my_car = Car("Sedan", common_wheel, common_wheel)

# Action
my_car.drive_over_nail()

# Result
print(my_car.get_wheel_statuses())

'''
What is the output of this script? 

Based on the line self.front_wheel.go_flat(), one might expect only the front wheel's status to change. 

Explain why the back wheel's status also changes.
We have two classes defined: a Wheel and a Car class. So we can see that these two classes have a relationship. The Car has a Wheel. So the Car and I can see from the following code as well that the Car is using delegation some of its responsibilities to the Wheel object. So in this relationship here, the Wheel object is a collaborator object for the Car.

All right, so let's look at the setup so that we can predict what the output of the script is. We have an instantiation of a Wheel and then we instantiate a Car object passing in the name of the car and two Wheel objects which have been assigned to the variable common wheel.

Then we have a method here drive over nil that is called upon the Car object (my car). In the drive over nil instance method, it is calling the Wheel objects (or rather, the method go flat is being called on the will object). So what it's going to return if we go to the will class definition is flat equals true.

So the results. Let's look at the result instead of how we print this. We call upon the get wheel statuses method (the calling object here is the Car object, my car object). We're going to print "Front wheel is flat" and actually what we did here is we called the drive over nil action and the drive over nil action has re-assigned the front wheel (or is flat instance variable to true). So the front wheel is flat equals true now.

And then this next second line "Back wheel is flat" is actually equals false because we did not call any method that would have updated the instance variable that is unique to the back wheel. Ah, I suppose actually that's not right. It has also changed because we actually passed the same object when we instantiated the car. So what we should have done really is we should have passed in two different objects for the back wheel and the front wheel as that way they would both have different states which is what we would expect. 

'''