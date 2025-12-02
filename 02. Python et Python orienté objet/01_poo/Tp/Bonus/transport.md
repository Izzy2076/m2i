# Exercice : Système de gestion des transports publics

## Description

Le système doit inclure les éléments suivants :

1. **Une classe `Vehicule`** :

   - Attributs :
     - `immatriculation` : Numéro d'immatriculation du véhicule.
     - `capacite` : Capacité maximale de passagers.
   - Méthode :
     - `afficher_informations()` : Affiche les informations générales du véhicule.

2. **Une classe `Electrique`** :

   - Attributs :
     - `capacite_batterie` : Capacité maximale de la batterie en kWh.
     - `niveau_charge` : Niveau actuel de la batterie en kWh.
   - Méthode :
     - `charger(kwh)` : Recharge la batterie.

3. **Une classe `Combustion`** :

   - Attributs :
     - `type_carburant` : Type de carburant utilisé (ex. Diesel, Essence).
     - `capacite_reservoir` : Capacité maximale du réservoir en litres.
     - `niveau_carburant` : Niveau actuel de carburant dans le réservoir.
   - Méthode :
     - `remplir_reservoir(litres)` : Remplit le réservoir de carburant.

4. **Une classe `BusHybride`** :

   - Hérite de `Vehicule`, `Electrique`, et `Combustion`.
   - Caractéristiques : Peut utiliser à la fois un moteur électrique et un moteur thermique.
   - Méthode :
     - `afficher_mode()` : Affiche les modes disponibles pour le bus hybride.

5. **Une classe `Tram`** :
   - Hérite de `Vehicule` et `Electrique`.
   - Caractéristiques : Fonctionne exclusivement en mode électrique.
   - Méthode :
     - `mode_tram()` : Indique que le tram fonctionne en mode électrique.

**Ajoutez des restrictions** dans `BusHybride` pour empêcher de rouler si :

- La batterie est déchargée.
- Le réservoir de carburant est vide.
