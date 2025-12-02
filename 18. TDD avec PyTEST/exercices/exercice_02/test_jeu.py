from jeu import initialiser_mot, reveler_lettre, victoire, tentatives

# init mot :

def test_initialiser_mot_simple():
    mot = "test"

    result = initialiser_mot(mot)

    assert result == "****"

def test_initialiser_mot_espace():
    mot = "test test"

    result = initialiser_mot(mot)

    assert result == "**** ****"

def test_initialiser_mot_vide():
    mot = ""

    result = initialiser_mot(mot)

    assert result == ""

# reveler lettre : 
    
def test_reveler_lettre_presente():
    lettre = "e"
    mot_cache = "****"
    mot_complet = "test"

    result = reveler_lettre(lettre, mot_cache, mot_complet)

    assert result == "*e**"

def test_reveler_lettre_presente_plusieurs_fois():
    lettre = "t"
    mot_cache = "****"
    mot_complet = "test"

    result = reveler_lettre(lettre, mot_cache, mot_complet)

    assert result == "t**t"

def test_reveler_lettre_absente():
    lettre = "a"
    mot_cache = "****"
    mot_complet = "test"

    result = reveler_lettre(lettre, mot_cache, mot_complet)

    assert result == "****"

def test_reveler_lettre_deja_presente():
    lettre = "t"
    mot_cache = "te*t"
    mot_complet = "test"

    result = reveler_lettre(lettre, mot_cache, mot_complet)

    assert result == "te*t"

def test_reveler_lettre_valide():
    lettre = "s"
    mot_cache = "te*t"
    mot_complet = "test"

    result = reveler_lettre(lettre, mot_cache, mot_complet)

    assert result == "test"

# Victoire
    
def test_victoire_true():
    mot_cache = "test"

    result = victoire(mot_cache)

    assert result == True

def test_victoire_false():
    mot_cache = "t*st"

    result = victoire(mot_cache)

    assert result == False

# tentatives
    
def test_tentatives_lettre_correct():
    nb_tentatives = 5
    lettre = "e"
    mot_complet = "test"

    result = tentatives(nb_tentatives, lettre, mot_complet)

    assert result == 5

def test_tentatives_lettre_incorrecte():
    nb_tentatives = 5
    lettre = "a"
    mot_complet = "test"

    result = tentatives(nb_tentatives, lettre, mot_complet)

    assert result == 4
    