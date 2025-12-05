class Animal:
    def __init__(self, name):
        self.name = name

class GoodDog(Animal):
    def __init__(self, color):
        super().__init__(color) # this is just going to be the 'name' in the superclass
        self.color = color # this is redundant

bruno = GoodDog("brown")
print(bruno)

'''
What is output and why? What does this demonstrate about super()?
We have two classes defined here:
1. Animal class with an initializer method
2. GoodDog class which inherits from Animal with its own initializer method
We also see a super function here which is going to act as a proxy class, allowing us to call the methods of the superclass. In line 10, we instantiate a GoodDog object and assign it to a variable called Bruno. Then we print Bruno. What is actually going to be printed?
In the instantiation, we pass in the value of brown to GoodDog. So now let's go to the GoodDog class. We see here that it's an initializer that inherits from the superclass and it accepts two arguments: self and color. It will take in except brown and then it reassigns as well the color brown. So think interestingly. Finally, we want to print Bruno. When we do print Bruno, I think is actually just going to print the default object representation or let me work this out. We seem to be missing an argument here.


'''

