from classes.Gateau import Gateau

mon_gateau = Gateau("Mon gâteau", 
                    120, 
                    ["Oeuf", "Farine", "Chocolat", "Lait"],
                    ["Étape 1", "Étape 2", "Étape 3"],
                    "Toto"
                    )

mon_gateau.afficher_ingredients()

mon_gateau.afficher_gateau()