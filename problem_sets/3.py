class Pet:
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'    

class Dog(Pet):
    def speak(self):
        return 'bark!'    

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring'


class Cat(Pet):
    def speak(self):
        return 'meow!'


teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!
print(teddy.fetch())

karl = Bulldog()
print(karl.speak())
print(karl.sleep())

kitty = Cat()
print(kitty.fetch())
