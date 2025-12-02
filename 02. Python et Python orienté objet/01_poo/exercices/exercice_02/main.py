from classes.CompteBancaire import CompteBancaire

compte = CompteBancaire()

compte.retrait(150)
compte.retrait(-150)

compte.versement(-150)
compte.versement(150)

compte.retrait(-1500)
compte.versement(1575)

compte.afficher()