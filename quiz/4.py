class Character:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '{self.name} is speaking.'

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

class Thief(Character):
    pass

sneak = Thief('Sneak')
print(sneak.name)             # Sneak
print(sneak.speak())          # Sneak is whispering.