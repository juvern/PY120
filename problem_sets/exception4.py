'''
Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.

Exceptions
- invalid value - within the list, contains strings
- division by zero - there is a zero

'''

def inverse_numbers(numbers: list):
    if not isinstance(numbers, list):
        return "The input should be a list"

    result = []

    for n in numbers:
        try:
            result.append(f'{1 / n:.2f}')
        except TypeError:
            result.append(None)
        except ZeroDivisionError:
            result.append('inf')

    return result


print(inverse_numbers('123')) # TypeError
print(inverse_numbers(123)) # TypeError
print(inverse_numbers([1, 2, 3]))
print(inverse_numbers([10, 20, 30, 40]))
print(inverse_numbers([10, 20, 'abc', 40])) # TypeError
print(inverse_numbers([10, 0, 30, 40]))