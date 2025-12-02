# import adn -> Import le module complet
from adn import saisie_adn, proportion # importe au cas par cas

chaine_adn = saisie_adn("Veuillez saisir la chaîne d'adn : ")
sequence_adn = saisie_adn("Veuillez saisir la séquence d'adn : ")

occurence = proportion(sequence_adn, chaine_adn)

print(f"Il y a {occurence} {sequence_adn} dans la chaîne : {chaine_adn}")