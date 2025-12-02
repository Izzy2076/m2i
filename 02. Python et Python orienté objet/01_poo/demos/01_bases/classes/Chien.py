# Par convention les classes commencent par une majuscule.
class Chien:
    # Constructeur
    def __init__(self, race, age, nom=None):
        self.nom = nom
        self.race = race
        self.age = age
        print(f"Naissance de {nom}")

    def aboyer(self):
        print(f"{self.nom} waf waf !")

    def aboyer_sur(self, chien):
        print(f"{self.nom} aboie sur {chien.nom}")
