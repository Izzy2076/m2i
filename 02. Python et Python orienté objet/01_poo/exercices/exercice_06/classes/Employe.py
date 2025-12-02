class Employe:
    compteur_id = 1

    def __init__(self, nom, salaire):
        self._nom = nom
        if salaire <= 0:
            raise ValueError
        self._salaire = salaire
        self._id_employe = Employe.compteur_id
        Employe.compteur_id += 1

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        if isinstance(nom, str):
            self._nom = nom
        else:
            raise ValueError
        
    @property
    def salaire(self):
        return self._salaire
    
    @salaire.setter
    def salaire(self, salaire):
        if isinstance(salaire, float):
            if salaire > 0:
             self._salaire = salaire
            else:
                raise ValueError
        else:
            raise ValueError
        
    @property
    def id_employe(self):
        return self._id_employe

    def presentation(self):
        return f"Je suis {self.nom},{self.__class__.__name__}. mon ID est {self.id_employe}, et mon salaire est de {self.salaire} €."
    
    def augmenter_salaire(self, pourcentage):
        self.salaire += self.salaire * (pourcentage/100)

    @classmethod
    def total_salaire(cls, equipe : list):
        return sum(emp.salaire for emp in equipe)