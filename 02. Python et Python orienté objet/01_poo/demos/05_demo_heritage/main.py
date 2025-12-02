from classes.Moto import Moto
from classes.Voiture import Voiture

v1 = Voiture("Voiture 1", "Rouge", "moteur1", 5)
m1 = Moto("Moto1", "Noir", "Moteur2", "Sport")

v1.demarrer()
print(v1.decrire())

m1.demarrer()
print(m1.decrire())