class Walkable:
    def walk(self):
        return "I'm walking."

class Swimmable:
    def swim(self):
        return "I'm swimming."

class Climbable:
    def climb(self):
        return "I'm climbing."

class Danceable:
    def dance(self):
        return "I'm dancing."

class Animal(Walkable):
    def speak(self):
        return "I'm an animal, and I speak!"

class GoodAnimals:
    class GoodDog(Animal, Swimmable, Danceable):
        pass

good_dog = GoodAnimals.GoodDog()
print(good_dog.walk()) # I'm walking.

mro_lst = GoodAnimals.GoodDog.mro()
print(mro_lst)

print([mro.__name__ for mro in mro_lst])
# ['GoodDog', 'Animal', 'Walkable', 'Swimmable', 'Danceable', 'object']

print(GoodAnimals.GoodDog.__mro__)

'''
What is the method lookup path used when invoking walk() on good_dog?

Let's go through the class definitions so we have:
- Walkable which has an instant method walk
- Swimmable which has an instant method called swim
- Climbable which has an instant method called climb
- Danceable with an instant method dance
We have animal that inherits from walkable with an instant method called speak.
Within the class "good animals", we have a nested class called "good dog" which inherits from animal, swimmable and danceable.
So then we come to line 25 where we see "good animals.good dog". This is the nested class object has been instantiated, and the "good dog" object inherits from animal, swimmable and danceable.
So following the MRO, we would first look at the class itself which is "good dog" and then we find no method called walk. So we would then move on to the animal class and then within the animal class we should also look at the animal super class which is walkable.
So when we look at walkable, we do see a method called walk, so this print statement will return "I am walking". However, if we don't find the walk instant method or within walkable, Python will keep going. It would then search for swimmable and finally you would also search for danceable. If it can't or it does not find the instant method, it will then search within the object itself, the object class that is.
So if we want to validate the MRO, we could also call the MRO method on the class itself to see what the MRO order is.

'''