class CompteBancaire:
    def __init__(self, numero_compte: int, nom : str, solde : int):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Vous avez ajouté {montant}€ à votre compte")
            print(f"Le nouveau solde est de {self.solde}€")
        else:
            print("Veuillez saisir un montant positif")

    def retrait(self, montant):
        if montant < 0:
            self.solde += montant
            print(f"Vous avez ajouté {montant}€ à votre compte")
            print(f"Le nouveau solde est de {self.solde}€")
            if self.solde < 0:
                self.agios()
        else:
            print("Veuillez saisir un montant négatif")
    
    def agios(self):
        if self.solde < 0:
            montant = self.solde * 0.05
            self.solde += montant
            print(f"5% appliqué pour un total de {montant}€")
            print(f"Le nouveau solde est de {self.solde}€")
        else:
            print("Votre compte est positif !")

    def afficher(self):
        print(f"Compte bancaire N°{self.numero_compte}")
        print(f"Appartient à : {self.nom}")
        print(f"Solde : {self.solde}")