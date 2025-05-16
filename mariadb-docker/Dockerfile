# Utiliser de l'image officielle de mariadb
FROM mariadb:10.11

# Définir un volume pour les données de la base
VOLUME ["/var/lib/mysql"]

# Installer le client MariaDB
RUN apt-get update && \
    apt-get install -y mariadb-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Définir les variables d’environnement MySQL
ENV MARIADB_ROOT_PASSWORD=root
ENV MARIADB_USER=edmond
ENV MARIADB_PASSWORD=adams001
ENV MARIADB_DATABASE=annuaires_student
ENV MARIADB_HOST=mariadb_cont

# Copie les fichiers d'initialisation
COPY init/ /docker-entrypoint-initdb.d/

# Expose le port 3306 pour les connexions à la base de données
EXPOSE 3306

# Définir la commande par défaut
CMD ["mysqld"]

