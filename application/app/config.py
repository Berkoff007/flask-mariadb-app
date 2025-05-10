import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_USER = os.getenv("MYSQLUSER", "root")
    DB_PASSWORD = os.getenv("MYSQLPASSWORD", "root")
    DB_HOST = os.getenv("MYSQLHOST", "localhost")
    DB_PORT = os.getenv("MYSQLPORT", "3306")
    DB_NAME = os.getenv("MYSQLDATABASE", "annuaires_student")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
