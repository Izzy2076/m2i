# TP PySpark

## Données fournies

- `clients.csv`
- `commandes.csv`

Chaque fichier contient des **données volontairement bruitées** : espaces parasites, casses incohérentes, valeurs manquantes, montants négatifs, devises multiples, commandes sans client associé.

### Schéma attendu

**clients.csv**

- `client_id:int`
- `nom:string`
- `prenom:string`
- `email:string`
- `phone:string`
- `city:string`
- `country:string`
- `signup_date:date`
- `segment:string`
- `is_vip:boolean`
- `birthdate:date`

**commandes.csv**

- `order_id:int`
- `client_id:int`
- `order_date:timestamp`
- `status:string`
- `amount:double`
- `currency:string`
- `payment_method:string`
- `items_count:int`
- `coupon_code:string`
- `city_shipping:string`
- `country_shipping:string`

## Objectifs :

3. Produire des statistiques avec **Spark SQL**.
4. Reproduire les mêmes résultats avec l’API **DataFrame**.
5. Manipuler différentes **jointures** pour détecter les anomalies et enrichir les analyses.
6. Exporter des résultats propres pour restitution.

## 1. Lire les deux CSV.

Afficher :

- Le schéma.
- 10 premières lignes.
- Nombre total de lignes.

## 2. Nettoyer et transformer vers une zone SILVER.

- Normalisation texte : suppression espaces, mise en minuscule/majuscule cohérente (nom, prenom, email, city, country, etc.).
- Validation email : transformer les emails invalides en NULL.
- Dates et types : cast correct de signup_date, birthdate, order_date.
- Montants :

  - Supprimer ou marquer comme invalides les montants ≤ 0.
  - Convertir USD en EUR avec un taux fixe (0,92).

- Persistance : sauvegarder en deux csv

## 3. Statistiques avec Spark SQL

- Créer des vues temporaires clients, commandes, commandes_clean.
- Réaliser les requêtes suivantes :
  - Chiffre d’affaires total (EUR).
  - CA par segment client (tri décroissant).
  - Panier moyen
  - Top 10 villes d’expédition
  - Taux (%) de commandes annulées ou retournées.
  - Clients sans commande.
  - Commandes sans client.

## 4. Statistiques équivalentes en DataFrame

- Reproduire exactement les mêmes résultats que ci-dessus, mais avec l’API PySpark

## 5. Exercices de Jointures

- INNER JOIN : clients et commandes_clean => CA et nb commandes par segment et country.
- LEFT JOIN : liste des clients avec nb commandes et CA (0 si aucune).
- RIGHT JOIN : comparer avec LEFT pour identifier commandes orphelines.
- FULL OUTER : détecter tout enregistrement sans correspondance.
- LEFT ANTI : clients sans aucune commande completed.
