# TP Python – Gestion de Commandes Clients

## Contexte

Une entreprise vend des produits informatiques. Elle possède un stock de produits et un historique de commandes clients. Elle souhaite un système capable de :

- Charger les produits existants et leur stock depuis un fichier CSV.
- Lire les commandes clients depuis un autre fichier CSV.
- Ajouter une nouvelle commande (si le stock le permet).
- Mettre à jour le stock en conséquence.
- Réécrire les fichiers CSV avec les nouvelles données.

### exemple `products.csv`

| id  | name      | price  | stock |
| --- | --------- | ------ | ----- |
| 1   | Clavier   | 49.99  | 15    |
| 2   | Souris    | 19.90  | 30    |
| 3   | Écran 24" | 129.00 | 8     |
| 4   | Webcam    | 39.99  | 20    |

### exemple`orders.csv`

| order_id | product_id | quantity | customer |
| -------- | ---------- | -------- | -------- |
| 1        | 1          | 2        | Toto     |
| 2        | 3          | 1        | Tata     |
| 3        | 2          | 3        | Titi     |

1. Les classes :

   - Créez une classe `Product` avec les attributs : `id`, `name`, `price`, `stock`.
   - Créez une classe `Order` avec : `order_id`, `product`, `quantity`, `customer`.
   - Créez une classe `OrderSystem` qui gère les collections de `Product` et `Order`.

2. **Chargement des données**

   - Implémentez des méthodes pour charger les produits et les commandes depuis leurs fichiers CSV.

3. **Ajout de commande**

   - Implémentez une méthode `add_order(product_id, quantity, customer)` :
     - Vérifie si le stock est suffisant.
     - Si oui, crée une commande, met à jour le stock du produit et incrémente l’ID de commande.

4. **Écriture dans les fichiers**

   - Réécrivez `products.csv` avec les nouveaux stocks.
   - Ajoutez la commande dans `orders.csv`.

5. **Affichages**
   - Affichez tous les produits avec leur stock actuel.
   - Affichez toutes les commandes.
   - Affichez la commande ajoutée si elle est acceptée.
