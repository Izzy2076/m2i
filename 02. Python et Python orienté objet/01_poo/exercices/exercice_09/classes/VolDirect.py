class VolDirect:
    def __init__(self, dep, arr, jour, heure):
        self._dep = dep
        self._arr = arr
        self._jour = jour
        self._heure = heure

    @property
    def dep(self):
        return self._dep

    @dep.setter
    def dep(self, value):
        if isinstance(value, str) :
            self._dep = value
        else:
            raise ValueError

    @property
    def arr(self):
        return self._arr

    @arr.setter
    def arr(self, value):
        if isinstance(value, str) :
            self._arr = value
        else:
            raise ValueError

    @property
    def jour(self):
        return self._jour

    @jour.setter
    def jour(self, value):
        if isinstance(value, str) :
            self._jour = value
        else:
            raise ValueError

    @property
    def heure(self):
        return self._heure

    @heure.setter
    def heure(self, value):
        if isinstance(value, int) :
            self._heure = value
        else:
            raise ValueError
        
    def afficher(self):
        return f"Ce vol part de {self.dep} vers {self.arr} le {self.jour} à {self.heure} heure"
