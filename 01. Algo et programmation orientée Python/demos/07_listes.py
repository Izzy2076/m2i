# On crée une liste avec des crochets []
#           0  1  2    3       4          5
ma_liste = [1, 2, 3, "test", True, ["a", "b", "c"]]

# Afficher un élément de ma liste (elle commence à l'index 0)
print(ma_liste[3])
print(ma_liste[-1][-1])
# ou
print(ma_liste[5][2])

ma_liste[4] = "toto"
# ma_liste[6] = "toto" -> la liste n'est pas assez grande donc erreur
print(ma_liste)

# Pour ajouter un élément à ma liste (toujours à la fin)
ma_liste.append(80)
ma_liste.append(1)
ma_liste.append(1)
print(ma_liste)

# Pour ajouter à un emplacement donné :
ma_liste.insert(0, "premier")
print(ma_liste)

# Pour ajouter une liste d'élément :
ma_liste.extend(["d", "e", "f"])
print(ma_liste)

# pour retirer un élément avec l'index et renvoyer l'élément :
test = ma_liste.pop(5)
print(ma_liste)
print(test)

# Pour retirer un élément via la valeur (uniquement le premier qui correspond)
ma_liste.remove(1)
print(ma_liste)

# Pour itérer sur une liste :
for element in ma_liste:
    print(element)