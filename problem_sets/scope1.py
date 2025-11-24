'''
Define a Dog class that has a breed instance variable. Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. Print the breed of each dog.
'''

class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"


maple = Dog("Golden Retriever")
bali = Dog("Poodle")
beanie = Dog("Labrador")
beanie._breed = "Jack Russell"
print(beanie.get_breed())


# print(maple.get_breed())
# print(bali.get_breed())

# chubbles = Cat()
# print(chubbles.get_name())