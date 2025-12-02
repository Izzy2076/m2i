# 5.1
# nb = int(input("Veuillez saisir un nombre : "))

# if nb % 3 == 0:
#     print(f"{nb} est divisible par 3")
# else:
#     print(f"{nb} n'est pas divisible par 3")

# 5.2
# nb_copies = int(input("Entrez le nombre de photocopies : "))

# if nb_copies <= 0:
#     print("Le nombre de photocopies ne peut pas être négatif")
# elif nb_copies < 10:
#     prix = nb_copies * 0.5
# elif nb_copies >= 10 and nb_copies <= 20:
#     prix = nb_copies * 0.4
# else:
#     prix = nb_copies * 0.3

# print(f"Le prix à payer est de {prix}€")

# 5.3
# age = int(input("Veuillez saisir l'âge de votre enfant : "))
# cat = None

# if age <= 0:
#     print("L'age ne peut pas être négatif")
# elif 3 <= age <= 6:
#     cat = "Baby"
# elif 7 <= age <= 8:
#     cat = "Poussin"
# elif 9 <= age <= 10:
#     cat = "Pupille"
# elif 11 <= age <= 12:
#     cat = "Minime"
# elif 13 <= age <= 18:
#     cat = "Cadet"
# else:
#     print("Votre enfant est trop agé !")

# print(cat)

# 5.4
# temp = int(input("Veuillez saisir la température de l'eau : "))

# if temp < 0 :
#     print("Solide")
# elif temp <= 100:
#     print("Liquide")
# else :
#     print("Gazeux")

# ternaire

# etat = "Solide" if temp < 0 else ("Liquide" if temp <= 100 else "Gazeux")

# print(etat)

# 5.5

# age = int(input("Veuillez saisir votre age : "))

# if age < 30:
#     print("Vous n'avez pas l'âge requis !")
#     exit()

# salaire = float(input("Veuillez saisir votre salaire : "))

# if salaire > 40000:
#     print("Salaire trop haut !")
#     exit()

# xp = float(input("Veuilelz saisir votre expérience : "))

# if xp < 5:
#     print("Vous n'avez pas l'expérience !")
#     exit()

# print("Vous avez tous les critères !")

# Autre méthode :

age = int(input("Veuillez saisir votre age : "))
salaire = float(input("Veuillez saisir votre salaire : "))
xp = float(input("Veuilelz saisir votre expérience : "))

if age >= 30:
    if salaire <= 40000:
         if xp >= 5:
              print("Vous avez tous les critères !")
         else:
              print("Vous n'avez pas l'expérience !")
    else:
         print("Salaire trop haut !")
else:
     print("Vous n'avez pas l'âge requis !")