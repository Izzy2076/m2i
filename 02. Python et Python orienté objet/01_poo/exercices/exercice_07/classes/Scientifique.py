from classes.Travailleur import Travailleur

class Scientifique(Travailleur):
    def __init__(self, prenom, tel, email, nom_entreprise, tel_pro, adresse_entreprise, disciplines, type_scientifique):
        super().__init__(prenom, tel, email, nom_entreprise, tel_pro, adresse_entreprise)
        self._disciplines = disciplines
        self._type_scientifique = type_scientifique

    @property
    def disciplines(self):
        return self._disciplines

    @disciplines.setter
    def disciplines(self, value):
        self._disciplines = value

    @property
    def type_scientifique(self):
        return self._type_scientifique

    @type_scientifique.setter
    def type_scientifique(self, value):
        self._type_scientifique = value

    def __str__(self):
        return f"{super().__str__()}, disciplines : {self.disciplines}, type : {self.type_scientifique}"
