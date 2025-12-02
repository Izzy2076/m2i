from classes.Vehicule import Vehicule

class Voiture(Vehicule):
    # Si aucun constructeur dans ma classe, on aura le constructeur de ma classe parent.
    def __init__(self, marque, couleur, motorisation, nb_portes):
        super().__init__(marque, couleur, motorisation)
        self.nb_portes = nb_portes

    # Surcharge de la méthode décrire
    def decrire(self):
        return f"{super().decrire()} - portes : {self.nb_portes}"