1. **Créer une classe abstraite `Instrument`** :

   - Ajoutez une méthode abstraite `jouer()` qui devra être implémentée par les sous-classes pour produire un son spécifique.
   - Ajoutez une méthode concrète `description()` qui affiche un message indiquant le type d'instrument.

2. **Implémenter au moins trois sous-classes d'instruments** :

   - Une classe `Guitare` qui implémente la méthode `jouer()` pour afficher :
     ```
     La guitare joue un air mélodieux.
     ```
   - Une classe `Piano` qui implémente la méthode `jouer()` pour afficher :
     ```
     Le piano joue une mélodie douce.
     ```
   - Une classe `Batterie` qui implémente la méthode `jouer()` pour afficher :
     ```
     La batterie frappe un rythme puissant.
     ```

3. **Créer une fonction `faire_jouer_les_instruments()`** :

   - Cette fonction prend en entrée une liste d'instances d'instruments.
   - Elle appelle successivement la méthode `description()` et la méthode `jouer()` pour chaque instrument.
