def initialiser_mot(mot):
    mot_cache = ""
    for c in mot:
        if c == " ":
            mot_cache += " "
        else:
            mot_cache += "*"
    return mot_cache

def reveler_lettre(lettre, mot_cache, mot_complet):
    nouveau_mot = ""
    for i in range(len(mot_complet)):
        if mot_complet[i] == lettre:
            nouveau_mot += mot_complet[i]
        else:
            nouveau_mot += mot_cache[i]
    return nouveau_mot

def victoire(mot_cache):
    return "*" not in mot_cache

def tentatives(nb_tentatives, lettre, mot_complet):
    if lettre not in mot_complet:
        nb_tentatives -= 1
    return nb_tentatives
