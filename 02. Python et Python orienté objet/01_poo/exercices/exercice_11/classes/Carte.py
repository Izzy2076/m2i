class Carte:
    couleurs = ["trèfle", "coeur", "carreau", "pique"]

    def __init__(self, valeur: int, couleur: str):
        if valeur < 2 or valeur > 14:
            raise ValueError("La valeur doit être entre 2 et 14")
        if couleur.lower() not in Carte.couleurs:
            raise ValueError("La couleur doit être Coeur, Trèfle, Carreau ou Pique")
        self._valeur = valeur
        self._couleur = couleur

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, value):
        if isinstance(value, int):
            self._valeur = value
        else:
            raise ValueError

    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self, value):
        if value in Carte.couleurs:
            self._couleur = value
        else:
            raise ValueError

    def __add__(self, other: "Carte"):
        return self.valeur + other.valeur
    
    def __sub__(self, other: "Carte"):
        return self.valeur - other.valeur
    
    def __gt__(self, other: "Carte"):
        return self.valeur > other.valeur
    
    def __lt__(self, other: "Carte"):
        return self.valeur < other.valeur
    
    def __eq__(self, other: "Carte"):
        return self.valeur == other.valeur
    
    def __contains__(self, couleur):
        return couleur in Carte.couleurs
    
    def __str__(self):
        return f"{self.couleur} - {self.valeur}"