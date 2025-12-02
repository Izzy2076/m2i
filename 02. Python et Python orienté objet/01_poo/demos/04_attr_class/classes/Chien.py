# Par convention les classes commencent par une majuscule.
class Chien:
    instances_chien = 0

    # Constructeur
    def __init__(self, race, age, nom=None):
        Chien.instances_chien += 1
        self.__nom = nom
        self._race = race
        self._age = age
        print(f"Naissance de {nom}")

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, nom):
        if isinstance(nom, str):
            self.__nom = nom
        else:
            raise ValueError
        
    @property
    def race(self):
        return self._race
    
    @race.setter
    def race(self, race):
        if isinstance(race, str):
            self._race = race
        else:
            raise ValueError
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise ValueError

    def aboyer(self):
        print(f"{self.nom} waf waf !")

    def aboyer_sur(self, chien):
        print(f"{self.nom} aboie sur {chien.nom}")

    @classmethod
    def afficher_nombre_chiens(cls):
        print(f"Il y a {cls.instances_chien} instanciés")
