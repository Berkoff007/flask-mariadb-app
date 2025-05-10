import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_USER = os.getenv("MYSQLUSER")
    DB_PASSWORD = os.getenv("MYSQLPASSWORD")
    DB_HOST = os.getenv("MYSQLHOST")
    DB_PORT = os.getenv("MYSQLPORT", "3306")
    DB_NAME = os.getenv("MYSQLDATABASE")  # <-- ici on prend 'railway'

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
