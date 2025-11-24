# Your code goes here
class Cat:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() == other.name.casefold()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() != other.name.casefold()

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() < other.name.casefold()

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() <= other.name.casefold()            

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() > other.name.casefold()

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() >= other.name.casefold()    

mindy = Cat('mindy')
mindy2 = Cat('MindY')

chubbles = Cat('chubbles')
chubbles2 = Cat('Chubbles')

blackie = Cat('blackie')

# print(mindy == mindy2)
# print(chubbles == chubbles2)
# print(mindy != chubbles)
# print(mindy2 != chubbles2)

print(mindy > chubbles)
print(blackie < chubbles)