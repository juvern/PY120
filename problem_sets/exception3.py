'''
Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.
'''
class NegativeNumberError(ValueError): # can also subclass Exception
    pass


user_input = input("Give me a number: ")

output = int(user_input)

if output < 0:
    raise NegativeNumberError("Negative number!")
else:
    print(f"The number is {output}")

