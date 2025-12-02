from classes.Vehicule import Vehicule

class Moto(Vehicule):
    def __init__(self, marque, couleur, motorisation, type_moto):
        super().__init__(marque, couleur, motorisation)
        self.type_moto = type_moto

    def decrire(self):
        return f"{super().decrire()} - type : {self.type_moto}"