import os

def lire_fichier(path):
    with open(path, "r", encoding="UTF-8") as file:
        secret = file.read()
    return secret

def ecrire_fichier(path, texte):
    with open(path, "w") as file:
        file.write(texte)

def main():
    file_path = "./exercices/exercice_14/secret.txt"

    if os.path.exists(file_path):
        secret = lire_fichier(file_path)
    else:
        secret = input("Veuillez saisir votre secret : ")

    while True:
        print("=== MENU ===")
        print("1. Voir le secret")
        print("2. Modifier le secret")
        print("0. Sauvegarder et quitter")

        choix = int(input("Veuillez faire votre choix : "))

        match choix:
            case 1 :
                print(f"Votre secret : {secret}")
            case 2 :
                secret = input("Modifier votre secret : ")
            case 0:
                ecrire_fichier(file_path, secret)
                exit()

main()