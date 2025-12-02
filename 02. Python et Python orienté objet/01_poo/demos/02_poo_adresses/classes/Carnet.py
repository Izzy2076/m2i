from classes.Address import Address

class Carnet:
    def __init__(self):
        self.adresses : list[Address] = []

    def input_address(self, address : Address=None):
        if address is None:
            print("==== Ajouter une adresse ====")
        else:
            print("==== Modifier une adresse ====")
            print("Entrée pour conserver l'ancienne valeure.")
            # if input("Veuillez saisir le numéro de voie : ") == "":

        numero_voie = input("Veuillez saisir le numéro de voie : ") or address.numero_voie
        complement = input("Veuillez saisir le complément : ") or address.complement
        intitule = input("Veuillez saisir l'intitulé : ") or address.intitule
        commune = input("Veuillez saisir la commune : ") or address.commune
        code_postal = input("Veuillez saisir le code postal : ") or address.code_postal

        return Address(numero_voie, complement, intitule, commune, code_postal)

    def display_address(self):
        print("==== Liste des adresses ====")
        for adresse in self.adresses:
            print(self.adresses.index(adresse) + 1, end=": ")
            print(adresse.to_string())

    def add_adresse(self):
        self.adresses.append(self.input_address())

    def edit_adresse(self):
        self.display_address()
        nb = int(input("Numéro de l'adresse à modifier : ")) - 1
        address = self.adresses[nb]
        self.adresses.pop(nb)
        self.adresses.insert(nb, self.input_address(address))

    def delete_adresse(self):
        self.display_address()
        nb = int(input("Numéro de l'adresse à supprimer : ")) - 1
        self.adresses.pop(nb)