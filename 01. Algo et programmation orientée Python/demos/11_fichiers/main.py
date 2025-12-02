import os

# chemin relatif
file_path = r"./demos/11_fichiers/fichier1.txt"
# chemin absolu
# file_path = r"C:\Users\Administrateur\Desktop\python\demos\11_fichiers\fichier1.txt"

# if os.path.exists(file_path):
#     file = open(file_path, "r")
#     data = file.read()
#     file.close()
#     print(data)
# else:
#     file = open(file_path, "w")
#     file.write("test")
#     file.close()

with open(file_path, "r") as file:
    data = file.read()
    print(data)

