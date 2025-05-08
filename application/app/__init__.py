from flask import Flask
from .config import Config
from .models import db

# Initialisation de l'application
app = Flask(__name__)
app.config.from_object(Config)  # <-- Ici, Config avec majuscule
db.init_app(app)

# Créer la base de données si elle n'existe pas
with app.app_context():
    print("start create_all...")
    db.create_all()
    print("end create_all...")

# Importer les routes après la création de l'application pour éviter les boucles
from app import routes
