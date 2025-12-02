from classes.Carnet import Carnet

carnet = Carnet()

def main():
    while True:
        print("==== MENU ====")
        print("1. Voir les adresses")
        print("2. Ajouter une adresse")
        print("3. Modifier une adresse")
        print("4. Supprimer une adresse")
        print("0. Quitter")

        choix = int(input("Veuillez faire votre choix : "))

        match choix:
            case 1:
                carnet.display_address()
            case 2:
                carnet.add_adresse()
            case 3:
                carnet.edit_adresse()
            case 4 :
                carnet.delete_adresse()
            case 0 :
                exit()
            case _:
                print("Erreur dans le choix !")

main()