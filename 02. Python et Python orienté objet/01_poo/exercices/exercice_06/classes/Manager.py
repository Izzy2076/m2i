from classes.Employe import Employe

class Manager(Employe):
    def __init__(self, nom, salaire, equipe):
        super().__init__(nom, salaire)
        self._equipe = equipe

    @property
    def equipe(self):
        return self._equipe
    
    @equipe.setter
    def equipe(self, equipe):
        if isinstance(equipe, list):
            self._equipe = equipe
        else:
            raise ValueError
        
    def ajouter_employe(self, employe):
        self.equipe.append(employe)

    def presentation(self):
        names = ", ".join([emp.nom for emp in self.equipe])
        return f"{super().presentation()} - Je supervise une équipe de {len(self.equipe)} personnes : {names}"