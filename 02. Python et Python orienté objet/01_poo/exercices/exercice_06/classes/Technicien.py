from classes.Employe import Employe

class Technicien(Employe):
    def __init__(self, nom, salaire, specialite):
        super().__init__(nom, salaire)
        self._specialite = specialite

    @property
    def specialite(self):
        return self._specialite
    
    @specialite.setter
    def specialite(self, specialite):
        if isinstance(specialite, str):
            self._specialite = specialite
        else:
            raise ValueError
        
    def changer_specialite(self, nouvelle_spe):
        self.specialite = nouvelle_spe

    def presentation(self):
        return f"{super().presentation()} - specialité : {self.specialite}"