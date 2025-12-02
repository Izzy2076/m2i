def verification_adn(chaine):
    for lettre in chaine.lower():
        # if lettre != "a" and lettre != "c" and lettre != "t" and lettre != "g":
        if lettre not in "atcg":
            return False
    return True

def saisie_adn(question):
    ma_chaine = input(question)

    while not verification_adn(ma_chaine):
        print("Erreur de saisie !")
        ma_chaine = input(question)
    
    return ma_chaine

def proportion(sequence : str, chaine : str):
    return chaine.count(sequence)

chaine_adn = saisie_adn("Veuillez saisir la chaîne d'adn : ")
sequence_adn = saisie_adn("Veuillez saisir la séquence d'adn : ")

occurence = proportion(sequence_adn, chaine_adn)

print(f"Il y a {occurence} {sequence_adn} dans la chaîne : {chaine_adn}")