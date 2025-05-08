from app import app, db

print('Starting the application...') 

if __name__ == '__main__':
    # Création de la base de données si elle n'existe pas
    with app.app_context():
        db.create_all()
        print('Database created successfully.') 

    # Lancement du serveur Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
