### Commandes de base

1. git init # Initialiser un nouveau dépôt Git
2. git config user.name "<name>" # Définissez votre nom d’utilisateur Git
3. git config user.email "<email>" # Définir votre adresse e-mail Git
4. git status # Vérifiez l’état de votre dépôt
5. git add <file> # Ajouter un fichier à la zone de staging
6. git add . # Ajouter tous les fichiers à la zone de staging
7. git commit -m "<message>" # Valider les modifications avec un message
8. git log # Afficher l’historique des commits
9. git log --oneline # Afficher l’historique des commits dans un format compact
10. git diff # Afficher les modifications entre le répertoire de travail et le dernier commit
11. git diff <branch1> <branch2> # Afficher les modifications entre deux branches
12. git show <commit> # Afficher les modifications apportées dans un commit spécifique
13. git ls-files # Répertorier tous les fichiers suivis par Git
14. git blame <file> # Montrer qui a modifié quoi dans un fichier
15. git bisect # Trouver le commit qui a introduit un bug
16. git reflog # Afficher un journal de tous les commits locaux
17. git cat-file -p <commit> # Afficher le contenu d’un objet commit
18. git rev-parse <ref> # Obtenir le hachage SHA-1 d’une référence
19. git fsck # Vérifier l’intégrité du référentiel
20. git gc # Nettoyez les fichiers inutiles et optimisez le dépôt

### Dépôts à distance

21. git remote add origin <url> # Connecter le dépôt local à la télécommande
22. git push -u origin <branch> # Pousser les modifications vers la branche distante
23. git pull # Extraire les modifications du dépôt distant
24. git clone <url> # Cloner un dépôt distant
25. git remote -v # Lister les connexions à distance
26. git remote rm <remote> # Supprimer une connexion à distance
27. git fetch # Récupérer les mises à jour du dépôt distant sans fusionner
28. git remote show <remote> # Afficher les détails d’un dépôt distant
29. git remote rename <old-name> <new-name> # Renommer un dépôt distant
30. git push --tags # Pousser toutes les balises vers le dépôt distant
31. git push --force # Forcer l’envoi des modifications au dépôt distant
32. git push origin --delete <branch> # Supprimer une branche distante
33. git pull --rebase # Extraire et rebaser la branche actuelle
34. git fetch --all # Récupérer les mises à jour de tous les dépôts distants
35. git remote update # Mettre à jour les branches de suivi à distance

### Branchement et fusion

36. git branch # Lister toutes les branches
37. git branch <branch> # Créer une nouvelle branche
38. git checkout <branch> # Passer à une branche
39. git checkout -b <branch> # Créer et passer à une nouvelle branche
40. git merge <branch> # Fusionner une branche dans la branche actuelle
41. git branch -d <branch> # Supprimer une branche
42. git branch -r # Lister les branches distantes
43. git branch -a # Répertorier les succursales locales et distantes
44. git branch -u <upstream-branch> # Définir la branche amont pour la branche actuelle
45. git branch -m <old-name> <new-name> # Renommer une branche
46. git branch --merged # Lister les branches qui ont été fusionnées dans la branche actuelle
47. git branch --no-merged # Répertorier les branches qui n’ont pas été fusionnées dans la branche actuelle
48. git merge --abort # Abandonner une opération de fusion en cours
49. git merge --squash <branch> # Écraser les commits d’une branche en un seul commit
50. git merge --no-ff <branch> # Fusionner avec un commit de fusion même s’il s’agit d’une fusion en avance rapide

### Stockage

51. git stash # Enregistrer les modifications pour plus tard
52. git stash list # Répertorier les modifications cachées
53. git stash apply # Appliquer les modifications cachées
54. git stash drop # Retirer une cachette
55. git stash pop # Appliquer et retirer la dernière réserve
56. git stash branch <branch> # Créez une nouvelle branche et appliquez une réserve
57. git stash save "<message>" # Enregistrer les modifications avec un message de stockage personnalisé
58. git stash clear # Supprimer toutes les modifications cachées
59. git stash apply <stash> # Appliquer une réserve spécifique
60. git stash drop <stash> # Retirer une réserve spécifique

### Rebase et sélection de cerises

61. git fetch # Récupérer les mises à jour à partir du dépôt distant
62. git rebase <branch> # Rebaser la branche actuelle sur une autre
63. git cherry-pick <commit> # Appliquer un commit spécifique
64. git rebase --abort # Abandonner une opération de rebase en cours
65. git rebase --continue # Poursuivre une opération de rebase suspendue
66. git rebase --skip # Ignorer un commit conflictuel lors du rebase
67. git cherry-pick --continue # Poursuivre une opération de sélection en pause
68. git cherry-pick --abort # Abandonner une opération de cherry-pick en cours

### Réinitialiser, supprimer et renommer

69. git reset # Réinitialiser la zone de staging pour qu’elle corresponde au dernier commit
70. git reset <file> # Supprimer un fichier de la zone de staging
71. git reset --hard # Ignorer toutes les modifications depuis le dernier commit
72. git rm <file> # Supprimer un fichier du référentiel et du répertoire de travail
73. git mv <old-name> <new-name> # Renommer ou déplacer un fichier
74. git clean -f # Supprimer les fichiers non suivis du répertoire de travail
75. git clean -fd # Supprimer les fichiers et répertoires non suivis du répertoire de travail

### Étiquettes

76. git tag # Balises de liste
77. git tag <tag-name> # Créer une balise légère
78. git tag -a <tag-name> -m "<message>" # Créer une balise annotée
79. git push origin <tag-name> # Envoyer une balise au dépôt distant
80. git tag -d <tag-name> # Supprimer un tag local
81. git push origin --delete <tag-name> # Supprimer une balise distante
82. git tag --contains <commit> # Trouver des balises contenant un commit spécifique
83. git describe # Décrivez le tag le plus récent et commit

### Commandes avancées

84. git submodule add <repository> <path> # Ajouter un sous-module Git
85. git submodule init # Initialiser les sous-modules Git
86. git submodule update # Mettre à jour les sous-modules Git
87. git submodule foreach <command> # Exécuter une commande dans tous les sous-modules
88. git grep <pattern> # Rechercher un motif dans le référentiel
89. git log -S"<pattern>" # Rechercher des commits qui ont ajouté ou supprimé un motif
90. git archive --format=zip --output=<output-file> <branch> # Créer une archive zip d’une branche
91. git shortlog # Résumer les journaux de commit par auteur
92. git log --graph --decorate --oneline # Afficher l’historique des commits sous forme de graphique
93. git rev-list --count <ref> # Compter le nombre de commits dans une branche
94. git commit --amend # Modifier le dernier commit
95. git commit --amend -m "<new-message>" # Modifier le dernier message de commit
96. git reflog expire --expire=now --all # Supprimer toutes les entrées de reflog
97. git rev-parse --show-toplevel # Afficher le répertoire racine du dépôt
98. git config --global alias.<alias-name> '<git-command>' # Créer un alias Git
99. git config --list # Lister tous les paramètres de configuration Git
100. git help <command> # Afficher l’aide pour une commande Git