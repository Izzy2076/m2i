import json, os

def charger_musiques(path):
    if os.path.exists(path):
        with open(path, "r", encoding="UTF-8") as file:
            liste_musiques = json.load(file)
    else:
        liste_musiques = []
    return liste_musiques

def sauvegarder_musiques(path, musiques):
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(musiques, file, indent=4, ensure_ascii=False)

def input_musique():
    titre = input("Veuillez saisir le titre de la chanson : ")
    artiste = input("Veuillez saisir l'artiste de la chanson : ")
    categorie = input("Veuillez saisir la catégorie de la chanson : ")
    while True:
        try:
            score = int(input("Veuillez saisir un score (sur 5) : "))
            if 0 <= score <= 5:
                break
            else:
                raise ValueError
        except ValueError:
            print("Il faut un score compris entre 0 et 5 !")
    return {"titre" : titre, "artiste" : artiste, "catégorie" : categorie, "score" : score}

def ajouter_musique(musiques: list):
    print("==== AJOUTER CHANSON ====")
    musiques.append(input_musique())

def modifier_chanson(musiques : list):
    print("==== MODIFIER CHANSON ====")
    afficher_musiques(musiques)
    choix = int(input("Veuillez saisir l'ID de la musique : ")) - 1

    try :
        musique = musiques[choix]

        if musique is not None:
            musique = input_musique()
            musiques.pop(choix)
            musiques.insert(choix, musique)
    except IndexError:
        print("Il n'y a pas de musique avec cet ID")

def afficher_musiques(musiques : list):
    if musiques != [] :
        print("==== AFFICHER LES CHANSONS ====")
        for musique in musiques:
            print(f"musique N°{musiques.index(musique) + 1}")
            for key, value in musique.items():
                print(f"{key} : {value}")
    else:
        print("Pas de musiques pour le moment")

def supprimer_chanson(musiques : list):
    print("==== SUPPRIMER CHANSON ====")
    afficher_musiques(musiques)
    choix = int(input("Veuillez saisir l'ID de la musique : ")) - 1

    try : 
        musique = musiques[choix]

        if musique is not None:
            musiques.pop(choix)
    except IndexError:
        print("Il n'y a pas de musique avec cet ID")

def main():
    file_path = "./exercices/exercice_16/datas/music.json"
    liste_musiques = charger_musiques(file_path)

    while True:
        print("==== MENU ====")
        print("1. Ajouter une chanson")
        print("2. Voir les chansons")
        print("3. Modifier une chanson")
        print("4. Supprimer une chanson")
        print("0. Quitter")

        choix = int(input("Veuillez faire votre choix : "))

        match choix:
            case 1:
                ajouter_musique(liste_musiques)
            case 2:
                afficher_musiques(liste_musiques)
            case 3:
                modifier_chanson(liste_musiques)
            case 4:
                supprimer_chanson(liste_musiques)
            case 0:
                sauvegarder_musiques(file_path, liste_musiques)
                exit()

main()