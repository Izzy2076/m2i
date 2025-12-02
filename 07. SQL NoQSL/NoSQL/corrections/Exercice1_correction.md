### **Exercice pratique**

Après avoir étudié les différents types de bases NoSQL, indiquez le **type de base** (clé-valeur, document, colonnes, graphe, multimodèle) le plus approprié pour chaque contexte applicatif.

1. Un réseau social doit analyser et visualiser les connexions entre utilisateurs, leurs amis, et leurs interactions.

Réponse : Graphe => Connexions complexes entre utilisateurs, exploration de relations

2. Une application e-commerce héberge des produits très différents les uns des autres (chaque produit a ses propres champs).

Réponse : Document => Données produits variées et flexibles, format JSON idéal

3. Un système de facturation génère des millions de transactions journalières à analyser rapidement en temps réel.

Réponse : Colonnes larges => Écritures massives et analyses efficaces, Big Data

4. Une API Web qui doit stocker et récupérer rapidement des sessions utilisateurs temporaires (durée de vie courte).

Réponse : Clé-valeur => Simplicité, rapidité pour stockage temporaire

5. Une plateforme de santé gère des dossiers patients très complexes avec des données structurées, semi-structurées et connectées (consultations, diagnostics, prescriptions, relations entre médecins).

Réponse : Multimodèle => Données mixtes : documents, relations, graphes

6. Une entreprise d’IoT collecte en continu des données de capteurs (température, humidité…) sur plusieurs millions de points.

Réponse : Colonnes larges => Données continues, compressées, lectures analytiques rapides

7. Un moteur de recommandation pour un site de streaming doit proposer des contenus basés sur les relations entre les utilisateurs, les films, les genres et les préférences.

Réponse : Graphe => Besoin d'analyser des relations pour la recommandation

8. Une application intelligente combine des données documentaires, relationnelles et de graphe dans un même système (ex. : assistant médical avec diagnostics, relations symptômes-maladies, données patient).

Réponse : Multimodèle => Nécessité de gérer documents, graphes et données relationnelles