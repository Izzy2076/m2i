## Jeu de données

- **Nom** : US-Accidents
- **Format** : CSV
- **Variables clés** :
  - `Severity` : niveau de gravité (1–4)
  - `Start_Time` : date et heure de l’accident
  - `State` : État
  - `City` : Ville
  - `Weather_Condition` : conditions météorologiques
  - Divers attributs de circulation et d’environnement

1. Préparation HDFS

2. Nombre d’accidents par État

- **Mapper** : extrait `State`, émet `<State, 1>`.
- **Reducer** : somme les valeurs pour chaque État.

3. Conditions météo

- **Mapper** : lit `Weather_Condition`, émet `<Condition, 1>`.
- **Reducer** : somme les occurrences.

4. Accidents aux heures de pointe

- **Mapper** : parse `Start_Time`, sélectionne si heure (6h–9h ou 16h–19h), émet `<City, 1>`.
- **Reducer** : somme les occurrences.

5. Gravité moyenne par État

- **Mapper** : émet `<State, Severity>`.
- **Combiner** : calcule partiellement somme et le nombre d'accidents.
- **Partitioner** : répartit les clés par État.
- **Reducer** : calcule moyenne de gravité par État.