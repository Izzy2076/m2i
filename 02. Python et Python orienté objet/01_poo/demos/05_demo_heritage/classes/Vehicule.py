class Vehicule:
    def __init__(self, marque, couleur, motorisation):
        self.marque = marque
        self.couleur = couleur
        self.motorisation = motorisation

    def demarrer(self):
        print(f"{self.marque} démarre.")

    def decrire(self):
        return f"{self.marque} - Couleur : {self.couleur} - Moteur : {self.motorisation}"