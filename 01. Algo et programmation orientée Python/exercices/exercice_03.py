import math

hauteur = float(input("Veuillez saisir la hauteur : "))
rayon = float(input("Veuillez saisir le rayon : "))

resultat = (math.pi * math.pow(rayon,2) * hauteur)/3
print(f"Volume : {round(resultat,2)}")