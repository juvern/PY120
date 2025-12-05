class Animal:
    def eat(self):
        print("I eat.")

class Fish(Animal):
    def eat(self):
        print("I eat plankton.")

class Dog(Animal):
    def eat(self):
        print("I eat kibble.")

def feed_animal(animal):
    animal.eat()

array_of_animals = [Animal(), Fish(), Dog()]
for animal in array_of_animals:
    feed_animal(animal)

'''
What is output and why? How does this code demonstrate polymorphism?

So, we first have the `Animal` class defined, and then the `Fish` class which inherits from `Animal`, and then the `Dog` class which also inherits from `Animal`.

We then have a function definition called `feedAnimal` with the parameter `animal`. And we then run the `feedAnimal` method call within that function.

In line 16, we actually instantiate a list of objects, an `Animal`, `Fish`, and `Dog` object. And then from 17 to 19, we have a for loop whereby for each `animal` in the list that we've created, we want to call the `feedAnimal` function passing in the value of each element of the array of `animals` list.

So, what this is going to output is the return value or the print. What this is going to output is the print statements that will be printed when we call `feedAnimal`. We called the method `feedAnimal` passing in the right. Let me just go back again.

So, what we then have here is in the for loop, we are actually going to be calling the function `feedAnimal`, and within that function, we're actually going to be calling the `eat` method for each `animal`. So, what we're going to then have is each of the instant methods in the objects called. So, we are going to print "I eat" in a first line, and then the `Fish` object, so to print "I eat plankton", `Dog` objects will print "I eat kibble".

So, this code here demonstrates polymorphism because we're able to run the same method across regardless of what object type it is. In this instance, `Animal`, `Fish`, and `Dog` are three different objects, and we did not have to care that they were different objects as long as they have the same method. And in this case, each of them has the same method `eat` which we were able to call and print the statement accordingly. It is normally advisable though to have the same type of output, as that way it would be easier to otherwise we wouldn't need to write too many different if statements to consider different types of outputs. 

'''