from classes.Personne import Personne
from classes.Scientifique import Scientifique
from classes.Travailleur import Travailleur

personne = Personne("toto", "0606060606", "toto@email.fr")
scientifique = Scientifique("Tata", "0606060606", "tata@email.fr", "Entreprise", "070707070", "adresse entreprise", ["Physique", "Chimie"], "Théorique")
travailleur = Travailleur("Titi", "0606060606", "tata@email.fr", "Entreprise", "070707070", "adresse entreprise")

print(personne)
print(scientifique)
print(travailleur)