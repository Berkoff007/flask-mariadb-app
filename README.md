# Flask + MariaDB App

Ce projet est une application web simple d'annuaire d'étudiants construite avec Flask et MariaDB.

## Structure
- `app/` : contient les fichiers principaux de l'application Flask.
- `Dockerfile` : instructions de construction de l'image Flask.
- `docker-compose.yml` : lance l'application Flask + base MariaDB en conteneurs.
- `run.py` : point d'entrée de l'application Flask.

## Lancer l'application en local
```bash
docker-compose up --build
```

## Accès
- Frontend : http://localhost:5000
- MariaDB : port 3306 (utiliser un client DB comme DBeaver ou MySQL Workbench)
```
