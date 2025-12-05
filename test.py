class LandDwellingMixin: pass
class BipedalismMixin: pass
class LanguageMixin: pass

class Creature: pass
class Mammal(Creature): pass
class Primate(LandDwellingMixin, Mammal): pass

class Human(Primate, BipedalismMixin, LanguageMixin):
    pass

mro_list = Human.mro()

print([mro.__name__ for mro in mro_list])
# ['Human', 'Primate', 'LandDwellingMixin', 'Mammal', 'Creature', 'BipedalismMixin', 'LanguageMixin', 'object']
