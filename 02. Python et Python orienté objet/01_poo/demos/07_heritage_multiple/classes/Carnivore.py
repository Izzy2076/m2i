from classes.EtreVivant import EtreVivant

class Carnivore(EtreVivant):
    def __init__(self,age):
        EtreVivant.__init__(self)
        self.age = age

    def se_nourrir(self):
        self.point_de_vie += 10

    def chasser(self):
        self.point_de_vie -= 1