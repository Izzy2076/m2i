# Exercice 02 : Jeu du pendu TDD

## Règles du jeu

- Un mot secret est choisi au début de la partie.
- Le joueur propose des lettres une par une.
- Si la lettre est présente, elle est révélée dans le mot.
- Si la lettre est absente, une tentative est retirée.
- Le joueur gagne s’il découvre le mot avant d’épuiser les tentatives.

## Étapes TDD

### Étape 1 — Initialisation du mot

Créer une fonction qui initialise le mot à deviner sous forme de caractères masqués.

### Étape 2 — Révélation d’une lettre

Créer une fonction qui met à jour l’état du mot lorsque le joueur propose une lettre correcte.

### Étape 3 — Vérification de la victoire

Créer une fonction qui détermine si le joueur a découvert entièrement le mot.

### Étape 4 — Gestion des tentatives

Créer une fonction qui met à jour le nombre de tentatives restantes selon la validité de la lettre proposée.

## Cycle TDD

1. **Red** : écrire un test qui échoue.
2. **Green** : écrire le code minimal pour le faire passer.
3. **Refactor** : améliorer le code sans casser les tests.
