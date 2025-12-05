class Person:
    def __init__(self, name):
        self.name = name
        self.pets = []

class Pet:
    def jump(self):
        print("I'm Jumping!")

class Cat(Pet):
    pass

class Bulldog(Pet):
    pass

bob = Person("Robert")
kitty = Cat()
bud = Bulldog()
bob.pets.append(kitty)
bob.pets.append(bud)
bob.pets.jump()

'''
We raise an error in the code below. Why? What do kitty and bud represent in relation to our Person object?

Okay, so what we have here are four different classes:
- Person
- Pet
- Cat
- Bulldog
We've got Person, we initialise a method, and then we've got Pet, which has one instance method called jump. Then we've got Cat that inherits from Pet, and another class, Bulldog, that also inherits from Pet.
So when we instantiate a Person object passing in the valley of Roberts, that would initialise the object with the state called name = 'Robert' and also another state or instance variable pets with an empty list.
And then we have kitty that has been assigned to an object called cat, but in this instance, there is no initialise method here. It will create an object, but there is no values initialised, same with Bulldog as well.
And then what we do in line 19 is append kitty to the instance variable pets. The instance variable is a list, so the append method will add the kitty object to that list, and the next one also adds the butt object, which is a Bulldog object to the list as well.
But then when we want to call jump, we're actually calling jump on the list, so the list itself doesn't have a method called jump. It is actually objects within all the elements within pets instance variable that has the instance method or that has the attribute or the method jump.
So to actually make it work as expected, we would have to use a for loop to access each element within the list that has been assigned to this pet. The instance variable, and in terms of what kitty and butt represents in relation to our Person object, it is a collaborator object because it is helping each other carry out its responsibilities. So Bob here or Person object here is calling the a method defined in the Pet class.

'''
