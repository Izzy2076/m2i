# Exercice : Gestion d'un réseau de transport

## Énoncé

Vous allez créer une classe `Bus` pour représenter les bus d'un réseau de transport public. Chaque bus possède des caractéristiques individuelles, mais aussi des informations globales qui s'appliquent à l'ensemble des bus.

---

### Étapes à suivre

1. **Créer la classe `Bus`**

   - Ajoutez un **attribut de classe** `total_bus` pour compter le nombre total de bus dans le réseau.
   - Ajoutez un **attribut de classe** `tarif_ticket` qui représente le tarif d'un ticket de bus (par défaut : 1,50 €).
   - Ajoutez un **attribut de classe** `capacite_max_globale` pour définir la **capacité maximale de passagers par bus** dans le réseau (par défaut : 50).

2. **Ajouter les attributs d'instance dans le constructeur (`__init__`)** :

   - `id_bus` : un identifiant unique pour le bus (entier).
   - `passagers` : le nombre actuel de passagers dans le bus (entier, initialisé à 0).

   > Chaque fois qu'un nouveau bus est créé, incrémentez l'attribut de classe `total_bus`.

3. **Ajouter les méthodes d'instance** :

   - `ajouter_passagers` : ajoute des passagers dans le bus, sans dépasser la capacité maximale définie pour les bus.
   - `retirer_passagers` : retire des passagers (sans descendre en dessous de 0).

4. **Ajouter les méthodes de classe** :

   - `modifier_tarif` : met à jour le tarif d'un ticket pour tous les bus.
   - `modifier_capacite_max_globale` : met à jour la capacité maximale globale des bus dans le réseau. Cette capacité doit s'appliquer à tous les bus nouvellement créés.
   - `afficher_statistiques` : affiche le nombre total de bus et le tarif actuel du ticket ainsi que leurs capacité.
