class Animal:
    def __init__(self):
        pass

class Bear(Animal):
    def __init__(self, color):
        super().__init__()
        self.color = color

bear = Bear("black")
print(bear)

'''
What is output and why? What does this demonstrate about super()?

So, what we have here are two classes that have been defined: `animal` and `bear`.

When we instantiate the object Bear.

The Bear's initializer method is called with the color='black'
super() represents the proxy class of the superclass which allows to call methods in the superclass. In this case we call the initializer in Animal passing in no argument. The initializer method in Animal does nothing. 

Then we assign black to the instance variable of `color`


'''

