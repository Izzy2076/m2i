from classes.Chien import Chien

rex = Chien(nom="rex", race="Berger allemand", age=12)
toto = Chien(nom="toto", race="Berger suisse", age=5)
chien = Chien("test", 15)
chien1 = Chien("test", 15)
chien2 = Chien("test", 15)

print(rex.instances_chien)
print(Chien.instances_chien)
print(toto.instances_chien)
toto.afficher_nombre_chiens()
Chien.afficher_nombre_chiens()

print(toto.nom)