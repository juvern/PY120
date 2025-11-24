class Person:

    # # doesn't validate when a constructor is invoked
    # def __init__(self, first_name, last_name): 
    #     self._first_name = first_name
    #     self._last_name = last_name

    def __init__(self, first_name, last_name):
        # validate each part
        self._validate(first_name)
        self._validate(last_name)
        
        # code only runs if validation passes
        self._first_name = first_name
        self._last_name = last_name

                            

    def _validate(self, name):
        if not name.isalpha():
            raise ValueError("Name must be alphabetic.") 

    @property
    def name(self):
        return f"{self._first_name.capitalize()} {self._last_name.capitalize()}"

    @name.setter
    def name(self, name):
        first, last = name

        # validate each part
        self._validate(first)
        self._validate(last)
        
        # code only runs if validation passes
        self._first_name = first
        self._last_name = last





actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.


# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# print(character.name)
# # ValueError: Name must be alphabetic.

# friend = Person('Lynn', 'Blake')
# print(friend.name)             # Lynn Blake
# friend.name = ('Lynn', 'Blake-John')
# print(friend.name)
# # ValueError: Name must be alphabetic.