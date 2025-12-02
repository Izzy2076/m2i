import csv, os

path = "./demos/12_csv/personne.csv"

with open(path, "r", encoding="UTF-8") as file:
    personnes = csv.reader(file, delimiter=";")
    next(personnes) # pour passer la première ligne
    for personne in personnes:
        print(personne)

with open(path, "a", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Titi", 25, "titi@email.fr"])
    csv.DictWriter
