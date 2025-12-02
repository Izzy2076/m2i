class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return (self.longueur + self.largeur) * 2
    
    def surface(self):
        return self.longueur * self.largeur