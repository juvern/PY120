'''
Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. 

In both cases, the function should return None when the element isn't found.
'''
numbers = [1, 2, 3, 4, 5]

def lbyl(numbers):
    if len(numbers) < 6:
        return None

    return numbers[5]

def afnp(numbers):
    try:
        return numbers[5]
    except IndexError:
        return None

print(lbyl(numbers))
print(afnp(numbers))