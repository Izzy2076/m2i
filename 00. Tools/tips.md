
### Mettre a jour Ubuntu WSL

1. sudo apt update && sudo apt upgrade -y

### Créer son environnement

1.  sudo apt install python3.12-venv
2.  créer son folder pour un projet , puis un sous folder genre dev, hml, prd et activer son venv en se positionnant dans le sous       folder souhaité
3.  python3 -m venv venv
4.  source /dev/bin/activate
5.  sudo apt install python3-pip
 

### Raccourci

1. Ctrl + : = commenter ligne ou bloc
2. Shift = indenter ligne ou bloc
3. Shift + tab = désindenter ligne ou bloc

### GIT

1.  git config --global user.name "stéphane.hermel"
2.  git config --global user.email "shermel76@gmail.com"
3.  ssh-keygen
4.  cat .ssh/id_ed25519.pub
5.  copier la cle publique ssh dans les parametres du github
6.  cd OneDrive_1_21-07-2025
7.  git init
8.  git add .
9.  git commit -m "ajout cours python"
10. git remote add origin git@github.com:Izzy2076/New.git
11. git push origin main


