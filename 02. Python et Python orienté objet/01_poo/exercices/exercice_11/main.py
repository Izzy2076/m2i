from classes.Carte import Carte

carte1 = Carte(5, "coeur")
carte2 = Carte(14, "Pique")

print(carte1)
print(carte2)

print(carte1 + carte2)
print(carte1 - carte2)
print(carte1 > carte2)
print(carte1 < carte2)
print(carte1 == carte2)

print("pique" in carte1.couleur)
print("coeur" in carte1.couleur)