'''
- what a collaborator object is
- code snippet
'''

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def introduce(self):
        for pet in self.pets:
            pet.greet()

class Pet:
    def __init__(self, breed):
        self.breed = breed

    def greet(self):
        print(f"I am a {self.breed}. Woof!")

bob = Owner('bob')
pet1 = Pet("Golden Retriever")
pet2 = Pet("Cockapoo")

bob.pets.append(pet1)
bob.pets.append(pet2)

bob.introduce()
