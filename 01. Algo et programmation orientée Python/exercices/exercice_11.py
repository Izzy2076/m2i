def operations(nb1, nb2):
    return nb1 + nb2, nb1 - nb2, nb1 * nb2, nb1/nb2 # packing


nb1 = float(input("Veuillez saisir un nombre : "))
nb2 = float(input("Veuillez saisir un nombre : "))
add, sub, mul, div = operations(nb1, nb2) # unpacking

print(add, div, sub, mul)
