# Utiliser une image officielle de Python
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet dans le conteneur
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Commande d'exécution
CMD ["python", "run.py"]
