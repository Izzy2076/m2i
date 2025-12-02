from classes.Personne import Personne

class Travailleur(Personne):
    def __init__(self, prenom, tel, email, nom_entreprise, tel_pro, adresse_entreprise):
        super().__init__(prenom, tel, email)
        self._nom_entreprise = nom_entreprise
        self._tel_pro = tel_pro
        self._adresse_entreprise = adresse_entreprise

    @property
    def nom_entreprise(self):
        return self._nom_entreprise

    @nom_entreprise.setter
    def nom_entreprise(self, value):
        self._nom_entreprise = value

    @property
    def tel_pro(self):
        return self._tel_pro

    @tel_pro.setter
    def tel_pro(self, value):
        self._tel_pro = value

    @property
    def adresse_entreprise(self):
        return self._adresse_entreprise

    @adresse_entreprise.setter
    def adresse_entreprise(self, value):
        self._adresse_entreprise = value

    def __str__(self):
        return f"{super().__str__()}, nom entreprise {self.nom_entreprise}, adresse entreprise : {self.adresse_entreprise}, tel pro : {self.tel_pro}"
