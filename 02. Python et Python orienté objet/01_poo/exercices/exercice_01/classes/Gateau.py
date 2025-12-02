class Gateau:
    def __init__(self, nom_gateau : str, temps_cuisson : int, ingredients : list[str], etapes: list[str], createur : str):
        self.nom_gateau = nom_gateau
        self.temps_cuisson = temps_cuisson
        self.ingredients = ingredients
        self.etapes = etapes
        self.createur = createur

    def afficher_ingredients(self):
        print("Les ingrédients :")
        for ingredient in self.ingredients:
            print(ingredient)

    def afficher_gateau(self):
        print(f"Recette pour {self.nom_gateau} par {self.createur}")
        self.afficher_ingredients()
        print("Les étapes : ")
        for etape in self.etapes:
            print(etape)
        print(f"Temps de cuisson : {self.temps_cuisson} minutes")