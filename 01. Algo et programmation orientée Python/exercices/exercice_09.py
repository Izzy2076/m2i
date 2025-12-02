import random

def choisir_nb_mystere(minimum, maximum):
    return random.randint(minimum, maximum)

def verifier_proposition(proposition, nb_mystere):
    if proposition == nb_mystere:
        print("Vous avez deviné le nombre mystère !")
        exit()
    elif proposition > nb_mystere:
        print("Le nombre mystère est plus petit")
    else:
        print("Le nombre mystère est plus grand")

def main():
    print("Bienvenue sur le nombre mystère")
    min = 1
    max = 100
    nombre_mystere = choisir_nb_mystere(min, max)
    essais = 5

    while essais > 0:
        print(f"Il vous reste {essais} essais.")

        while True:
            proposition = int(input(f"Veuillez saisir un nombre entre {min} et {max} : "))
            if min <= proposition <= max:
                break

        verifier_proposition(proposition, nombre_mystere)
        essais -= 1
    
    if essais == 0:
        print(f"Vous avez perdu, le nombre mystère était {nombre_mystere}")

main()