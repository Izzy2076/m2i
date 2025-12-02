# JSON => JavaScript Object Notation
# pour créer un dictionnaire :
mon_dict = {}

toto = {
    "prenom" : "Toto",
    "age" : 25,
    "email" : "toto@email.fr",
    "isAdmin" : False
}

tata = {
    "prenom" : "Tata",
    "age" : 25,
    "email" : "tata@email.fr",
    "isAdmin" : False
}

titi = {
    "prenom" : "Titi",
    "age" : 25,
    "email" : "titi@email.fr",
    "isAdmin" : False
}

print(toto)

# Pour accéder à la valeur, nous passons par la clé
print(toto["prenom"])
toto["age"] += 1
print(toto)

# Pour ajouter une clé/valeur
# toto["telephone"] = "0606060606"
# print(toto)

# Pour supprimer une clé/valeur
# del toto["isAdmin"]
# print(toto)

for value in toto.values():
    print(value)

for key in toto.keys():
    print(key)
    
for key, value in toto.items():
    print(f"{key} = {value}")

annuaire = [toto, tata, titi]

print("-" * 50)

for personne in annuaire:
    for key, value in personne.items():
        print(f"{key} = {value}")
    print("-" * 50)

# CRUD => Create, Read, Update, Delete