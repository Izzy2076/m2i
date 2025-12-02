class Address:
    def __init__(self, numero_voie, complement, intitule, commune, code_postal : int):
        self.numero_voie = numero_voie
        self.complement = complement
        self.intitule = intitule
        self.commune = commune
        self.code_postal = code_postal

    def to_string(self):
        return f"Numéro de voie : {self.numero_voie}, complément {self.complement}, intitulé : {self.intitule}, commune : {self.commune}, code postal : {self.code_postal}"