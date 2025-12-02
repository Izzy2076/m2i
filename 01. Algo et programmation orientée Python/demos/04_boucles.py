# for i in range(1, 101):
#     print(i)

# Itération avec un pas de 2
for i in range(1, 101, 2):
    print("la valeur de i =", i)

increment = 0

while increment < 10:
    increment += 1

    if increment == 3:
        continue # On passe à l'itération suivante, les instructions suivantes ne sont pas exécutées

    if increment == 7:
        break # On arrête complétement la boucle sans faire les itérations suivantes

    print(increment)

# resultat = 15

# while resultat < 150000:
#     resultat *= 10
#     print(resultat)