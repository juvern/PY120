'''
What is output and why? What does this demonstrate about instance variables?

'''
class Swimmable:
    def enable_swimming(self):
        self._can_swim = True

class Dog(Swimmable):
    def swim(self):
        if hasattr(self, '_can_swim') and self._can_swim:
            return "swimming!"
        return None

teddy = Dog()
print(teddy.swim())

