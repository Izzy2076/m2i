class Bus:
    total_bus = 0
    tarif_ticket = 1.50
    capacite_max = 50

    def __init__(self, id_bus, passagers = 0):
        if passagers > Bus.capacite_max or passagers < 0:
            raise ValueError("Impossible de créer un nouveau bus")
        self._id_bus = id_bus
        self._passagers = passagers
        Bus.total_bus += 1

    @property
    def passagers(self):
        return self._passagers
    
    @passagers.setter
    def passagers(self, passagers):
        if isinstance(passagers, int):
            self._passagers = passagers
        else:
            raise ValueError

    def ajouter_passager(self, nb):
        if self.passagers + nb > Bus.capacite_max:
            print(f"Impossible d'ajouter {nb} passagers")
        else:
            self.passagers += nb
            print(f"{nb} passagers ajoutés, passagers actuel : {self.passagers}")

    def retirer_passager(self, nb):
        if self.passagers - nb < 0:
            print(f"Impossible de retirer {nb} passagers")
        else:
            self.passagers -= nb
            print(f"{nb} passagers retirés, passagers actuel : {self.passagers}")

    @classmethod
    def modifier_tarif(cls, nouveau_tarif):
        cls.tarif_ticket = nouveau_tarif
        print(f"Le tarif du ticker a été mis à jour : {nouveau_tarif}€")

    @classmethod
    def modifier_capacite(cls, nouvelle_capacite):
        cls.capacite_max = nouvelle_capacite
        print(f"La capacité est maintenant de : {nouvelle_capacite} personnes")

    @classmethod
    def afficher_statistiques(cls):
        print(f"Nombre total de bus : {cls.total_bus}")
        print(f"Prix du ticket : {cls.tarif_ticket}")
        print(f"capacité max : {cls.capacite_max}")
    
