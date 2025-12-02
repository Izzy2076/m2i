# 7.1
def nom_complet(prenom : str, nom : str):
    return f"{prenom.title()} {nom.title()}"

nom = nom_complet("John", "Doe")
print(nom)
print(nom_complet("John", "Doe"))

# 7.2
def soustraire(a : int, b : int) -> int:
    print(f"je soustrait {a} et {b}")
    return a - b

print(soustraire(1, 2))

# 7.3
def quelle_heure(heure : str = "12h00") -> None:
    print(heure)

quelle_heure()
quelle_heure("14h00")

# 7.4
def compter_lettre_a(chaine : str) -> int:
    count = 0
    for lettre in chaine.lower():
        if lettre == "a":
            count += 1
    return count

print(compter_lettre_a("Abba"))
print(compter_lettre_a("mixer"))