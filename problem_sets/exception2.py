'''
Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential ZeroDivisionError or ValueError exceptions (there is no need to retry inputs in this problem).
'''

dividend = input("Give me a number: ")
divisor = input("Now give me another number: ")
print("We are going to divide the two numbers.")
try:
    dividend = float(dividend)
    divisor = float(divisor)
    result = dividend / divisor
except (ValueError, ZeroDivisionError) as e:
    print(f"Invalid. Original error - {e}")
finally:
    print("End of the program")

'''
- float expects a str
- but the str value is the wrong value hence ValueError

'''
