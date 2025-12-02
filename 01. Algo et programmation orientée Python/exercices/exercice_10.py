# 10.1
# ma_liste = []

# for i in range(0,10):
#     ma_liste.append(i)

# print(f"Le chiffre à la 9éme place est : {ma_liste[8]}")

# 10.2
# for i in range(1, 16):
#     nb = int(input(f"Veuillez saisir la note n°{i} : "))
#     ma_liste.append(nb)

# print(ma_liste)

# 10.3

# while True:
#     note = float(input("Veuillez saisir une note entre 0 et 20 (une note négative stoppera la saisie) : "))
#     if note < 0:
#         break
#     elif 0 <= note <= 20:
#         ma_liste.append(note)
#     else:
#         print("Note erronée !")

# print(f"La note maximale est de {max(ma_liste)}/20")
# print(f"La note minimale est de {min(ma_liste)}/20")
# print(f"La moyenne des notes est de  {sum(ma_liste)/len(ma_liste)}/20")

# 10.4
participants = ["toto1", "toto2", "toto3", "toto4", "toto5", "toto6", "toto7"]

def panne_moteur():
    # Suppression du premier participant
    premier = participants.pop(0)
    # Ajout du participant en dernière position
    participants.append(premier)

panne_moteur()
print(participants)

def passe_en_tete():
    # swap de variables
    tmp = participants[0]
    participants[0] = participants[1]
    participants[1] = tmp
    
passe_en_tete()
print(participants)

def sauve_honneur():
    # swap de variables
    tmp = participants[-1]
    participants[-1] = participants[-2]
    participants[-2] = tmp

sauve_honneur()
print(participants)

def tir_blaster():
    return participants.pop(0)

participant = tir_blaster()
print(participants)

def retour_inattendu(participant):
    participants.append(participant)

retour_inattendu(participant)
print(participants)