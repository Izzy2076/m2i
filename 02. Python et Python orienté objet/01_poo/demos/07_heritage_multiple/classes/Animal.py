from classes.EtreVivant import EtreVivant

class Animal(EtreVivant):
    def __init__(self, nom):
        EtreVivant.__init__(self)
        self.nom = nom

    def se_nourrir(self):
        self.point_de_vie += 5

    def dormir(self):
        self.point_de_vie += 1