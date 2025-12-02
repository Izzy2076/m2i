from classes.Chien import Chien

rex = Chien(nom="rex", race="Berger allemand", age=12)
toto = Chien(nom="toto", race="Berger suisse", age=5)
chien = Chien("test", 15)

toto.nom = 15
print(toto.nom)
