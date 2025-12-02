class Chien:
    def __init__(self, nom, age, taille, race):
        self.nom = nom
        self.age = age
        self.taille = taille
        self.race = race

    def __str__(self):
        return f"{self.nom} - age : {self.age} - taille : {self.taille} - race : {self.race}"

    def __len__(self):
        return self.taille
    
    def __repr__(self): # information pour le dev
        return f"{self.__class__.__name__}(nom={self.nom}, age={self.age}, taille={self.taille}, race={self.race})"
    
    def __int__(self):
        return self.age
    
    def __bool__(self):
        return self.age > 3
    

rex = Chien("Rex", 8, 45, "Husky")

print(rex) # -> __str__
print(len(rex)) # -> __len__
print(repr(rex)) # -> __repr__
print(int(rex)) # -> __int__
print(bool(rex)) # -> __bool__