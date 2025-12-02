# 6.1
# while True:
#     nb = int(input("Veuillez saisir un nombre entre 1 et 3 compris : "))
#     if 1 <= nb <= 3:
#         break
#     else:
#         print("Erreur ! veuillez saisir un nombre entre 1 et 3 compris")

# 6.2
# capital_initial = float(input("Veuillez saisir un capital de départ : "))
# taux = float(input("Veuillez saisir un taux : "))/100
# capital_final = 0
# annees = 0

# while capital_final < capital_initial * 2:
#     annees += 1
#     capital_final = capital_initial * (1 + taux)**annees
#     print(round(capital_final,2))

# print(f"Le capital doublera en {annees} années")

# 6.3
# print("Table de 9 :")
# for i in range(1,11):
#     print(f"9 X {i} = {9*i}")

# 6.4
# nb_max = None

# for i in range(1,7):
#     nb = int(input("Veuillez saisir un nombre : "))
#     if i == 1:
#         nb_max = nb
#     if nb > nb_max:
#         nb_max = nb

# print(nb_max)

# avec try ... except
# nb_max = None

# for _ in range(6):
#     try:
#         nb = int(input("Veuillez saisir un nombre : "))
#         if nb > nb_max:
#             nb_max = nb
#     except TypeError:
#         nb_max = nb
#     except ValueError:
#         print("Erreur, veuillez saisir un nombre !")



# print(nb_max)

# 6.5
# pop = int(input("Veuillez saisir la population : "))
# pop_visee = int(input("Veuillez saisir la population visée : "))
# taux = float(input("Veuillez saisir le taux d'accroissement : "))/100
# annees = 0

# while pop < pop_visee:
#     pop *= 1 + taux
#     annees += 1

# print(f"La population dépasse la population visée : {annees} années")

# 6.6
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)