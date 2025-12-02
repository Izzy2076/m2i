import math
# Les opérateur arithmétiques

addition = 4 + 4
multiplication = 4 * 4
division = 4 / 2
division_entiere = 5 // 2
puissance = 5 ** 2 # 5^2
modulo = 5 % 2 # modulo -> reste de la division

addition = addition + 4
# opérateur unaire
addition += 4
addition -= 5

# Concatenation
hello_world = "hello" + " " + "world"
print(hello_world)
print("-" * 50)
print(math.pi)

# Les opérateurs de comparaison
print(25 > 1) # supérieur à
print(25 >= 1) # supérieur ou égal
print(25 < 1) # inferieur à
print(25 <= 1) # inferieur ou égal
print(25 == 1) # strictement égal à
print(25 != 1) # différend de

print("-" * 50)

# Opérateurs logiques
print((25 > 1) and (25 != 50)) 
print((25 > 1) or (25 == 50))
print("xor :")
print((25 > 1) ^ (25 == 50)) # XOR => seulement une des deux conditions est vraie mais pas les deux
print(not True) # Inversion