CREATE DATABASE scooter_mov;
USE scooter_mov;

CREATE TABLE IF NOT EXISTS fabricantes (
    id_fabricante INT NOT NULL AUTO_INCREMENT,
    denominacion VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL,
	PRIMARY KEY(id_fabricante)
) ENGINE=InnoDB;

CREATE TABLE scooters (
    id_scooter INT NOT NULL AUTO_INCREMENT,
    color VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    velocidad_maxima INT NOT NULL,
    bateria INT NOT NULL DEFAULT 100,
    velocidad_actual INT NOT NULL DEFAULT 0,
    encendida BOOLEAN NOT NULL DEFAULT 0,
    id_fabricante INT,
    PRIMARY KEY (id_scooter),
    FOREIGN KEY (id_fabricante) REFERENCES fabricantes(id_fabricante)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

INSERT INTO fabricantes (denominacion, pais) 
VALUES 
    ('Xiaomi', 'China'),
    ('Segway-Ninebot', 'USA'),
    ('Ather Energy', 'India'),
    ('Gogoro', 'Taiwan');
    
    INSERT INTO scooters (color, marca, modelo, velocidad_maxima, bateria, velocidad_actual, encendida, id_fabricante) 
VALUES 
    ('Negro', 'Xiaomi', 'Mi Electric Scooter Pro 2', 25, 100, 0, 0, 1),       
    ('Blanco', 'Segway-Ninebot', 'Ninebot Max', 30, 80, 10, 1, 2),           
    ('Verde', 'Ather Energy', '450X', 40, 90, 20, 0, 3),                     
    ('Gris', 'Gogoro', 'Viva Mix', 50, 70, 30, 1, 4),                       
    ('Rojo', 'Segway-Ninebot', 'Ninebot ES2', 25, 50, 15, 0, 2),             
    ('Azul', 'Xiaomi', 'Mi Electric Scooter Essential', 20, 60, 5, 1, 1);   
    
SELECT DISTINCT COLOR FROM SCOOTERS;

SELECT id_scooter, marca, modelo, velocidad_actual 
FROM scooters 
WHERE encendida = 1;

SELECT id_scooter, color, marca, bateria 
FROM scooters 
WHERE bateria < 50;

SELECT marca, modelo, velocidad_maxima 
FROM scooters 
ORDER BY velocidad_maxima DESC;

SELECT DISTINCT PAIS FROM FABRICANTES;


