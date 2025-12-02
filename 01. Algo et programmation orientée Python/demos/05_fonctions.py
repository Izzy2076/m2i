def hello_world():
    print("test")
    print("un autre print")

hello_world()
hello_world()
hello_world()
hello_world()

prenom = "test" # Variable global

def bonjour_qui(prenom): # prenom est une variable local
    print(f"Bonjour {prenom}")

bonjour_qui("Toto")
bonjour_qui("Tata")
bonjour_qui("Titi")

def bonjour_qui_defaut(age : int, prenom="Test"):
    print(f"Bonjour {prenom}")

bonjour_qui_defaut(18)
bonjour_qui_defaut(25, "toto")

def addition(a : int, b : int) -> int :
    resultat = a + b # variable local
    print("test")
    return resultat

resultat = addition(1, 2)
resultat2 = addition(1, 3)
print(resultat)
print(resultat2)

a = 10

def fonction():
    a += 1


mot = "test"

for lettre in mot:
    print(lettre)