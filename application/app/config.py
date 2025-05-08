import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_USER = os.getenv('MARIADB_USER', 'root')
    DB_PASSWORD = os.getenv('MARIADB_PASSWORD', 'root')
    DB_NAME = os.getenv('MARIADB_DATABASE', 'annuaires_student')
    DB_HOST = os.getenv('MARIADB_HOST', 'db')  # "db" = nom du service Docker
    DB_PORT = os.getenv('MARIADB_PORT', '3306')  # Port explicite

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
