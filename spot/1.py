class Person:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    def set_name(self):
        self._name = 'Bob'

bob = Person()
print(bob.name)

'''

What we have here is a class that has been defined called Person. Within the class itself, we've got an initializer method, where the instance variable _name has been assigned to None. And then we can see that we've got a property decorator, so we've got a getter property here, a getter property method, which returns the _name instance variable. We also then have what it looks like a setter property, but it doesn't actually have the property decorator, which assigns the _name to Bob. So what we then see in line 12, we instantiate a new object instance of person. And then when we finally go about printing Bob.name, we are actually going to just print None in this instance because in the initializer _name is assigned to None and.name notation here. The attribute here is just going to return the instance variable _name. Which is actually None.
''' 
