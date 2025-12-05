class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}."

class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner # A Person object

    def bark(self):
        return f"{self.name} says Woof!"

owner = Person("Bob")
dog = Dog("Buddy", owner)

# We can access the collaborator object's methods like this:
print(f"My owner is {dog.owner.name}.")
print(dog.owner.greet())

'''
Predict the output and explain the relationship between the Dog and Person classes. Why is composition (using a collaborator object) a more suitable design here than having Dog inherit from Person?

We have two classes defined: one called 'person' and one called 'dog'. Within each of these classes, we have an initializer method and also another instance method.

When we go to line 16, we can see that we have instantiated an object 'person' passing in the value of 'bop'. So, what that does is the initializer method would run. The instance variable 'name' will be assigned to 'bob'. And then, we've got a new object that is also instantiated in the next line. Here, we've got an object called 'dog' where we pass in the value of 'buddy', which will be assigned to the instance variable 'name'. We also pass in a 'person' object as the owner attribute as the value to the owner attribute. Then, we're able to print'my owner is accessing the dog object on the owner attribute', and then the owner attributes 'name' attribute, which will be 'Bob'. When we call 'greet' on the 'dog'.owner, we're actually calling 'greet' on the 'person' object. So, there is no is-a relationship here; a dog isn't a person, nor is a person a dog. More accurately, it's a has-a relationship - a dog has an owner, and using collaborator objects makes this relationship more flexible. You can see that this is a collaborative relationship because here, a dog has and owner which is a Person object. The Dog object, to carry out its responsibilities, is using the Person object, its collaborator object.

'''
    