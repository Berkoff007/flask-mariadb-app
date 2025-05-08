import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'

     # Config de la base de données
    if os.environ.get('FLASK_ENV') == 'docker':
        SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:root@db/annuaires_student'
    else:
        SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:root@localhost/annuaires_student'
    
    #config mysql installation locale 
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/annuaire_student'
    
    #config mariadb installation locale 
    #SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:root@localhost/annuaire_students'
    
    #config contenaire mariadb nom:db
    #SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:password@db/annuaire_student'

    #config sqlite installation locale or via contenaire 
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///annuaire_student.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()