adresses = []

def display_address():
    print("==== Liste des adresses ====")
    for address in adresses:
        print(adresses.index(address) + 1, end=": ")
        for key, value in address.items():
            if value:
                print(f"{key} : {value}", end=", ")
        print()

def input_address(address=None):
    if address is None:
        address = {}
        print("==== Ajouter une adresse ====")
    else:
        print("==== Modifier une adresse ====")
        print("Entrée pour conserver l'ancienne valeure.")
        # if input("Veuillez saisir le numéro de voie : ") == "":

    address["numeroVoie"] = input("Veuillez saisir le numéro de voie : ") or address.get("numeroVoie", "")
    address["complement"] = input("Veuillez saisir le complément : ") or address.get("complement", "")
    address["intitule"] = input("Veuillez saisir l'intitulé : ") or address.get("intitule", "")
    address["commune"] = input("Veuillez saisir la commune : ") or address.get("commune", "")
    address["codePostal"] = input("Veuillez saisir le code postal : ") or address.get("codePostal", "")

    return address

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
                display_address()
            case 2:
                adresses.append(input_address())
            case 3:
                display_address()
                nb = int(input("Numéro de l'adresse à modifier : ")) - 1
                address = adresses[nb]
                input_address(address)
            case 4 :
                display_address()
                nb = int(input("Numéro de l'adresse à supprimer : ")) - 1
                adresses.pop(nb)
            case 0 :
                exit()
            case _:
                print("Erreur dans le choix !")

main()