class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

martin = Student('Martin')
john = Student('John')

# discouraged as it's obscures the fact that it's a class variable
print(martin.school_name) 

# encouraged for readability
print(martin.__class__.school_name)



print(f"{john.name} read at {john.__class__.school_name}")
print(f"{martin.name} read at {martin.__class__.school_name}")