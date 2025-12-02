from classes.VolDirect import VolDirect
from classes.Vols import Vols

def saisie_jours():
    jours= ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

    while True:
        jour = input("Veuillez saisir un jour : ")
        if jour in jours:
            return jour
        else:
            print("Jour invalide !")

def saisie_heure():
    while True:
        heure = int(input("Veuillez saisir l'heure de départ : "))
        if 0 <= heure < 24:
            return heure
        else:
            print("Heure invalide !")

def saisie_ville():
    return input("Veuillez saisir la ville : ")

lv = []

for i in range(3):
    print("Ajouter un vol :")
    dep = saisie_ville()
    arr = saisie_ville()
    jour = saisie_jours()
    heure = saisie_heure()

    lv.append(VolDirect(dep, arr, jour, heure))

vols = Vols(lv)

print("Liste des vols : ")
vols.affiche()

ville = saisie_ville()

if vols.appartient(ville):
    print(f"La ville {ville} fait partie du plan de vol !")
else:
    print(f"La ville {ville} ne fait pas partie du plan de vol !")

print(f"LEs villes accessibles depuis {ville} sont : {vols.liste_successeurs(ville)}")