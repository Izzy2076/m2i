# Par convention les classes commencent par une majuscule.
class Chien(object):
    # Constructeur
    def __init__(self, race, age, taille, nom=None):
        self.nom = nom
        self.race = race
        self.age = age
        self.taille = taille
        print(f"Naissance de {nom}")

    def aboyer(self):
        print(f"{self.nom} waf waf !")

    def aboyer_sur(self, chien):
        print(f"{self.nom} aboie sur {chien.nom}")

    def __str__(self):
        return f"Nom : {self.nom} - Race : {self.race} - Age : {self.age}"
    
    def __len__(self):
        return self.taille
