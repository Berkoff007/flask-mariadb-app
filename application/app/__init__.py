from flask import Flask
from sqlalchemy import text
from .config import Config
from .models import db

# Initialisation de l'application
app = Flask(__name__)
app.config.from_object(Config)  # <-- Ici, Config avec majuscule
db.init_app(app)

# Vérification de la connexion à la base de données
with app.app_context():
    try:
        print("✅ Tentative de connexion à la base de données...")
        db.session.execute(text("SELECT 1"))
        print("✅ Connexion à la base de données réussie.")
    except Exception as e:
        print("❌ Erreur de connexion à la base de données :")
        print(e)

    print("start create_all...")
    db.create_all()
    print("end create_all...")

# Importer les routes après la création de l'application pour éviter les boucles
from app import routes
