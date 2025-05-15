# Utiliser une image officielle de Python
FROM python:3.9-slim-buster
# Définir le répertoire de travail
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    wget \
    libmariadb3 \
    libmariadb-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Installations de connecteur MariaDB C
RUN wget https://dlm.mariadb.com/2678574/Connectors/c/connector-c-3.3.3/mariadb-connector-c-3.3.3-debian-bullseye-amd64.tar.gz -O - | \
    tar -zxf - --strip-components=1 -C /usr


# Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet dans le conteneur
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Commande d'exécution
CMD ["python", "run.py"]
