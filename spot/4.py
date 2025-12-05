'''
What is output? 

Is this what we would expect when using AnimalClass.__add__? 

If not, how could we adjust the implementation of AnimalClass.__add__ to be more in line with what we'd expect the method to return?

'''
class AnimalClass:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def __lshift__(self, animal):
        self.animals.append(animal)
        return self

    # def __add__(self, other_class):
    #     result = self.animals + other_class.animals
    #     return [animal.name for animal in result]
    def __add__(self, other_class):
        new_class = AnimalClass(f"{self.name} and {other_class.name}")
        new_class.animals = self.animals + other_class.animals
        return new_class

class Animal:
    def __init__(self, name):
        self.name = name

mammals = AnimalClass('Mammals')
mammals << Animal('Human')
mammals << Animal('Dog')
mammals << Animal('Cat')
birds = AnimalClass('Birds')
birds << Animal('Eagle')
birds << Animal('Blue Jay')
birds << Animal('Penguin')
some_animal_classes = mammals + birds
print(some_animal_classes)

'''
 
'''