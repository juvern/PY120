'''
What is output and why? What does this demonstrate about constant scope? What does self refer to in each of the 3 methods above?
'''

class Describable:
    def describe_shape(self):
        return f"I am a {self.__class__.__name__} and have {self.SIDES} sides."

class Shape(Describable):
    @classmethod
    def sides(cls):
        return cls.SIDES

    def sides_instance(self):
        return self.__class__.SIDES

class Quadrilateral(Shape):
    SIDES = 4

class Square(Quadrilateral):
    pass

print(Square.sides())
print(Square().sides_instance())
print(Square().describe_shape())

'''
Okay, so what we've got here are four classes:
- Describable has a class method called describeShape
- The class Shape inherits from Describable and has a class method called Sites
- Quadrilateral inherits from Shape
- Square inherits from Quadrilateral
So let's first figure out what Square.Sites is going to print. In line 23, we call upon the method Sites in the class Square. So when we look into Square, there is no such method, so let's go up the inheritance chain. Let's look at Quadrilateral. Again, there is no such method called Sites, so let's go up to Shape instead. When we look into Shape, we now actually do see a class method called Sites. So what it's going to do then is return the value for class.Sites, which is equivalent to saying square.Sites. So now let's go up the chain again. Do we have a constant or a variable looking at this? It's in all caps, it suggests that it's a constant variable. Do we have that constant variable in Square? No, we don't. So we go up to Quadrilateral and then we see 4. Finally, this line is going to print the value of 4.
Let's look at line 24. This is calling the method SitesInstance on an instance of a square object, so we'll keep going up the chain. We don't have the Sites instance in Square, so we go out to Quadrilateral. No, we don't. So we go up to Shape and now we see SitesInstance Method. Here, it's saying return this class of the self, which is actually very similar to the one before. Self double underscore class is actually the same as saying square.sides, so it will print the same value as line 23, which is going to be 4.
Let's go to the next one where we have to go and look for the method called describeShape. When we start in Square, there's none. We go to Quadrilateral, there's none, so we go to Shape, there's none, and then we finally go to Describable where we find it. Here, it's going to return us a string, "I am a self dunder class name and have self.sides". The class name here is Square, and it is also going to have 4 sides as well. So it's going to finally print, "I am a square and have 4 sides".
So what does this demonstrate about Constant Scope? Constant Scope follows the method resolution order, where it would first look for it in the class that it's called if not, it's going to look into the classes that it inherits from.
And what about what does self refer to in each of these three methods? Self here refers to the object itself, the calling object. In all three cases, that is square.
'''