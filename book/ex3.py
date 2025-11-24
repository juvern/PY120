class Car:
    def __init__(self, plate, year, color):
        self._plate = plate
        self._year = year
        self.color = color # triggers the setter

    def __str__(self):
        return f"{self.color.capitalize()} {self._year} {self._plate}"

    def __repr__(self):
        return f"Car({repr(self._plate)}, {repr(self._year)}, {repr(self.color)})"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color # where the color is set

    @property
    def plate(self):
        return self._plate

    @property
    def year(self):
        return self._year

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz.color)         # red

print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')