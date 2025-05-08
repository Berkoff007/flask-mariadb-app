CREATE DATABASE IF NOT EXISTS annuaires_student;

USE annuaires_student;

CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Insertion de données initiales dans la table `students`
INSERT INTO student (first_name, last_name, email) VALUES
('Adamou', 'edmond', 'adamouedmond7@gmail.com'),
('Gorba', 'osee', 'oseegorba@gmail.com'),
('Adingue', 'frederic', 'adinguefrederic@gamail.com'),
('Djamra', 'randandi', 'djamrarandandi@gamail.com'),
('Ruth', 'amadjibeye', 'ruthamadjibeye@gamail.com');