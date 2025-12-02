import csv

path = "./exercices/exercice_15/produits.csv"

titre = input("Titre du produit : ")
prix = input("Prix du produit : ")
stock = input("Stock du produit : ")

data = [titre, prix, stock]

with open(path, "a", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(data)