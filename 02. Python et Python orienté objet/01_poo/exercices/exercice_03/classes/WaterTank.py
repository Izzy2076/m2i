class WaterTank:
    all_watertanks = 0

    def __init__(self, poids : float, capacite_max : float, remplissage : float):
        self._poids = poids
        self._capacite_max = capacite_max
        self._remplissage = remplissage
        WaterTank.all_watertanks += remplissage
    
    @property
    def poids(self):
        return self._poids
    
    @poids.setter
    def poids(self, poids):
        if isinstance(poids, float):
            self._poids = poids
        else:
            raise ValueError
        
    @property
    def capacite_max(self):
        return self._capacite_max
    
    @capacite_max.setter
    def capacite_max(self, capacite_max):
        if isinstance(capacite_max, float):
            self._capacite_max = capacite_max
        else:
            raise ValueError
        
    @property
    def remplissage(self):
        return self._remplissage
    
    @remplissage.setter
    def remplissage(self, remplissage):
        if isinstance(remplissage, float):
            self._remplissage = remplissage
        else:
            raise ValueError
        
    def poids_total(self):
        return f"Le poids total de ma citerne est de : {self.poids + self.remplissage} Kg"
    
    def remplir(self, valeur):
        if self.remplissage + valeur <= self.capacite_max:
            self.remplissage += valeur
            WaterTank.all_watertanks += valeur
        else:
            WaterTank.all_watertanks += self.capacite_max - self.remplissage
            self.remplissage = self.capacite_max
            print("Impossible de remplir plus la citerne !")
        print(f"La citerne fait maintenant {self.remplissage}L")

    def vider(self, valeur):
        if self.remplissage - valeur > 0:
            self.remplissage -= valeur
            WaterTank.all_watertanks -= valeur
            print(f"La citerne fait maintenant {self.remplissage}L")
        else:
            WaterTank.all_watertanks -= self.remplissage
            self.remplissage = 0.0
            print("La citerne est vide !")