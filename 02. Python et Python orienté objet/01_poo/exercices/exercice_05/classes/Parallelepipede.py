from classes.Rectangle import Rectangle

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        # largeur * longueur * hauteur
        return super().surface() * self.hauteur
    
    def perimetre(self):
        # 4 * (hauteur + largeur + longueur)
        return 4 * (self.hauteur + self.largeur + self.longueur)
    
    def surface(self):
        # 2 * largeur * longueur + 2 * longueur * hauteur + 2 * largeur * hauteur
        return 2 * super().surface() + 2 * self.longueur * self.hauteur + 2 * self.largeur * self.hauteur