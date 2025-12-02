# Utilise une image de base avec python 3.11.9 en version minimal
FROM python:3.11.9-slim

# Création d'un nouvel utilisateur non root
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Définit le répértoire de travail (création du dossier)
WORKDIR /app

# Copie les fichiers app.py et requirements.txt dans /app
COPY . .

# Installation des dépendances Python
RUN pip install -r requirements.txt

USER appuser

# Ouvre le port 5000 dans le conteneur
EXPOSE 5000

# python app.py
# CMD [ "python", "app.py" ]
# Commande par défaut : lance l'application
ENTRYPOINT [ "python", "app.py" ]

# docker build -t myapp:1.0
