from classes.Animal import Animal
from classes.Carnivore import Carnivore

class Toutou(Carnivore, Animal):
    def __init__(self, nom, age):
        Animal.__init__(self, nom)
        Carnivore.__init__(self, age)

    def se_nourrir(self):
        Animal.se_nourrir(self)