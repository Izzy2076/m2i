import random

def creer_personnage(nom, classe):
    return {
        "nom": nom,
        "classe" : classe,
        "niveau" : 1,
        "pointsDeVie" : 100,
        "inventaire" : [
            {"nom" : "potion_de_soin", "quantite" : 3}
        ]
    }

# def ajouter_objet(inventaire, nom, quantite):
#     for item in inventaire:
#         if item["nom"] == nom:
#             item["quantite"] += quantite
#             break         
#     else:
#         inventaire.append({"nom" : nom, "quantite" : quantite})

# avec kwargs :

def ajouter_objet(inventaire, **objets):
    for nom, quantite in objets.items():
        for item in inventaire:
            if item["nom"] == nom:
                item["quantite"] += quantite
                break         
    else:
        inventaire.append({"nom" : nom, "quantite" : quantite})

def modifier_statistiques(personnage):
    personnage["niveau"] += 1
    personnage["pointsDeVie"] += 20

def utiliser_potion(personnage):
    for item in personnage["inventaire"]:
        if item["nom"] == "potion_de_soin" and item["quantite"] > 0:
            item["quantite"] -= 1
            points_gagnes = random.randint(1, 50)
            personnage["pointsDeVie"] += points_gagnes
            print(f"{personnage["nom"]} gagne {points_gagnes} points de vie !")
            if item["quantite"] == 0:
                personnage["inventaire"].remove(item)
            break

def afficher_personnage(personnage):
    print(f"Nom : {personnage["nom"]}")
    print(f"Classe : {personnage["classe"]}")
    print(f"Niveau : {personnage["niveau"]}")
    print(f"Point de vie : {personnage["pointsDeVie"]}")
    for item in personnage["inventaire"]:
        print(f"- {item["nom"]} (quantité : {item["quantite"]})")

toto = creer_personnage("Toto", "Guerrier")
titi = creer_personnage("Titi", "Mage")

afficher_personnage(toto)

print("-" * 50)

ajouter_objet(toto["inventaire"], Pomme=5)
ajouter_objet(toto["inventaire"], Pomme=5, Epee=1, Bouclier=1 )
afficher_personnage(toto)

print("-" * 50)

for _ in range(10):
    modifier_statistiques(toto)
afficher_personnage(toto)

print("-" * 50)


afficher_personnage(toto)

# Bonus
def attaquer(attaquant, adversaire):
    degats = 10 * attaquant["niveau"]
    adversaire["pointsDeVie"] -= degats
    print(f"{attaquant["nom"]} attaque {adversaire["nom"]} et inflige {degats} points de dégats")

    if adversaire["pointsDeVie"] <= 0:
        print(f"{adversaire["nom"]} est vaincu !")
        print(f"{attaquant["nom"]} récupére : ")

        for item in adversaire["inventaire"]:
            print(f"{item["quantite"]} X {item["nom"]}")
            ajouter_objet(attaquant["inventaire"], **item)
        
        adversaire["inventaire"] = []

print("======== ATTAQUE ========")

attaquer(toto, titi)
afficher_personnage(toto)
afficher_personnage(titi)
# pour modifier plusieurs éléments : 'ctrl + h + h'