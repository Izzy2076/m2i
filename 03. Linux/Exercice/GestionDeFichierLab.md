
# 🧪 **Fondamentaux Linux – TP de Gestion Avancée des Fichiers**

---

## 🎓 **Scénario**

Tu es un administrateur système Linux junior.

Ton équipe utilise le répertoire `/srv/projects/` pour stocker des journaux (`logs`), fichiers temporaires, et scripts provenant de plusieurs utilisateurs.

Ta mission est de :

* Inspecter et nettoyer ce répertoire
* Appliquer les bonnes permissions et appartenances
* Archiver les anciens journaux
* Supprimer de manière sécurisée les données sensibles
* Utiliser les commandes avancées `find`, `ls`, `chmod`, `chown`, `stat`, `tar`, et `shred`
* T'exercer avec `-exec {} \;` et `-exec {} +`

---

## 🧰 **Préparation de l’environnement – (Pour l’instructeur uniquement)**

> 💡 Lancer les commandes suivantes avant le TP pour simuler un répertoire de projet réel.

```bash
sudo mkdir -p /srv/projects
sudo chown "$USER:$USER" /srv/projects
cd /srv/projects

# Simuler des fichiers .log anciens (mars 2024)
touch -t 202403010101 file1.log
touch -t 202403080101 file2.log
touch -t 202403150101 file3.log

# Créer des fichiers volumineux (~100 Mo+)
dd if=/dev/zero of=bigfile1.tmp bs=1M count=110
dd if=/dev/zero of=bigfile2.tmp bs=1M count=120

# Créer un fichier confidentiel avec des permissions non sécurisées
echo "secret data" > password.txt
chmod 777 password.txt

# Ajouter un fichier temporaire de debug
echo "temporary debug info" > debug.tmp
chmod 777 debug.tmp

# Ajouter un script shell
echo -e '#!/bin/bash\necho Hello' > cleanup.sh
chmod 644 cleanup.sh
```

---

## 📂 **PARTIE 1 : Analyse et inspection des fichiers**

### 1.1 Lister tous les fichiers dans `/srv/projects/` avec des infos détaillées, triés par taille (du plus gros au plus petit), avec des tailles lisibles humainement 


### 1.2 Lister tous les fichiers triés par date de modification, du plus ancien au plus récent


### 1.3 Afficher le vrai type de chaque fichier (analyse du contenu, pas juste l’extension) 



---

## 🔐 **PARTIE 2 : Gestion des permissions et accès**

### 2.1 Modifier les permissions de `password.txt` pour que seul le propriétaire puisse lire et écrire 


### 2.2 Trouver tous les fichiers `.sh` dans le dossier et les rendre exécutables **seulement** par leur propriétaire 

---

## 🔎 **PARTIE 3 : Filtrage et nettoyage**

### 3.1 Trouver et lister tous les fichiers de plus de 100 Mo dans `/srv/projects` 

### 3.2 Trouver et lister tous les fichiers modifiés il y a plus de 7 jours

---

## 📦 **PARTIE 4 : Archivage**

### 4.1 Archiver tous les fichiers `.log` modifiés il y a plus de 7 jours dans une archive compressée gzip

 ➤ Enregistrer l’archive dans `~/backups/` sous le nom `old_logs_<date_du_jour>.tar.gz`

---

## 🧹 **PARTIE 5 : Suppression sécurisée**

### 5.1 Supprimer de façon sécurisée le fichier `password.txt` en écrasant son contenu avant suppression

---

## 📊 **PARTIE 6 : Rapports et propriétaires**

### 6.1 Afficher les métadonnées (taille, dates, numéro d’inode, etc.) pour chaque fichier `.log` 

### 6.2 Compter combien de fichiers dans `/srv/projects/` sont possédés par l’utilisateur courant 


