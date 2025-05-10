import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")

    DB_USER = os.getenv("MYSQLUSER")
    DB_PASSWORD = os.getenv("MYSQLPASSWORD")
    DB_NAME = os.getenv("MYSQLDATABASE")
    DB_HOST = os.getenv("MYSQLHOST")
    DB_PORT = os.getenv("MYSQLPORT", "3306")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
