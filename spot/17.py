import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        # Find the greatest common divisor
        common = math.gcd(numerator, denominator)

        # Simplify the numerator and denominator
        self.numerator = numerator // common
        self.denominator = denominator // common


    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        new_value = 

    def __eq__(self):
        pass

    def __str__(self):
        pass

# Example Usage:
frac1 = Fraction(1, 2)
frac2 = Fraction(1, 4)
frac3 = Fraction(2, 4)

print(frac1 + frac2)  # Expected output: 3/4
print(frac1 == frac2) # Expected output: False
print(frac1 == frac3) # Expected output: True
print(frac3)          # Expected output: 1/2 (since it should be simplified on initialization or representation)