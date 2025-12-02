import json

path = "./demos/13_json/personne.json"

# le méthode .dump() permet d'écrire dans un fichier json
# with open(path, "w", encoding="UTF-8") as file:
#     mon_dict = [{"prenom" : "Toto", "age": 25, "email" : "toto@email.fr"}, {"prenom" : "Toto", "age": 25, "email" : "toto@email.fr"}]
#     # indent sert à avoir une présentation plus esthétique
#     json.dump(mon_dict, file, indent=4) 

with open(path, "r", encoding="UTF-8") as file:
    personnes = json.load(file)
    print(personnes)