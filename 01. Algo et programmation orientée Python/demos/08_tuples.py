def recuperer_nombre_carre(nombre):
    return nombre, nombre**2 # tuple packing -> on se sert d'un tuple pour retourner plusieurs valeurs

print(recuperer_nombre_carre(5))

# unpacking : on 'decoupe' notre tuple en plusieurs valeurs
nombre, carre = recuperer_nombre_carre(9)
print(nombre)
print(carre)

mon_tuple = 1, 2, 3, 4, 5

var1, var2, var3, var4, var5 = mon_tuple

# La variable "_" dans python sert à se débarasser de valeurs inutiles
var1, var2, _, _, var5 = mon_tuple
