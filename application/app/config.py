import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'

    # Configuration de la base de données
    if os.environ.get('FLASK_ENV') == 'docker':
        # Assurez-vous que 'db' correspond bien au nom de votre conteneur MariaDB
       SQLALCHEMY_DATABASE_URI = f"mariadb+pymysql://{os.environ.get('MARIADB_USER')}:{os.environ.get('MARIADB_PASSWORD')}@db/{os.environ.get('MARIADB_DATABASE')}"
    else:
        SQLALCHEMY_DATABASE_URI = 'mariadb+pymysql://root:root@localhost/annuaires_student'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()
