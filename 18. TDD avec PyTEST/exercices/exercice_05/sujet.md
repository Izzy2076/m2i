# Exercice 05

Vous recevez un fichier `produits_bruts.csv` contenant les colonnes suivantes :

- `id` : identifiant du produit
- `nom` : nom du produit
- `categorie` : catégorie du produit
- `prix` : prix en euros (format texte)
- `stock` : quantité en stock (format texte)

## Problèmes identifiés dans les données

1. **Noms de produits** : espaces inutiles en début/fin, casse incohérente
2. **Catégories** : majuscules/minuscules mélangées, espaces parasites
3. **Prix** : format texte au lieu de numérique, valeurs invalides possibles
4. **Stock** : valeurs négatives (erreurs de saisie), format texte
5. **Lignes invalides** : produits sans nom

Votre pipeline doit nettoyer les données selon ces règles :

### 1. Normalisation des noms de produits

- Supprimer les espaces en début et fin
- Title Case

### 2. Normalisation des catégories

- Convertir en **minuscules**
- Supprimer les espaces en début et fin

### 3. Conversion des prix

- Convertir en type **float**
- Les valeurs invalides doivent devenir **None**

### 4. Correction du stock

- Convertir en type **integer**
- Les valeurs **négatives** doivent être mises à **0**

### 5. Suppression des lignes invalides

- Supprimer les produits dont le **nom est vide ou null**

Pour chaque fonction, écrivez des tests unitaires.
