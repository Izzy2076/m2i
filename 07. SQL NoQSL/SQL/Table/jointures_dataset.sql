USE formation_sql;

DROP TABLE IF EXISTS Utilisateur;
DROP TABLE IF EXISTS Abonnements;

CREATE TABLE Utilisateur ( 
	id INT PRIMARY KEY AUTO_INCREMENT, 
	first_name VARCHAR(100), 
	last_name VARCHAR(100), 
	city VARCHAR(100), 
	age INT 
); 

INSERT INTO Utilisateur (first_name, last_name, city, age) VALUES
('Alice', 'Durand', 'Paris', 28),
('Bruno', 'Martin', 'Lyon', 35),
('Clara', 'Lemoine', 'Marseille', 22),
('David', 'Petit', 'Paris', 40),
('Eva', 'Bernard', 'Lille', 31),
('Félix', 'Roux', 'Nice', 29),
('Gabriel', 'Faure', 'Lyon', 45),
('Hélène', 'Morel', 'Toulouse', 27);

CREATE TABLE Abonnements ( 
	client_id INT, 
	abonnement_type VARCHAR(100)
);

INSERT INTO Abonnements (client_id, abonnement_type) VALUES
(1, 'Premium'),
(2, 'Standard'),
(3, 'Étudiant'),
(4, 'Premium'),
(6, 'Premium'),
(7, 'Standard'),
(8, 'Étudiant'),
(999, 'Test');
