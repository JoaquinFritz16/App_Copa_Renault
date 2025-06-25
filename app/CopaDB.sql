DROP DATABASE IF EXISTS copa_renault;
CREATE DATABASE copa_renault;
USE copa_renault;
CREATE TABLE Colegios (
  id_colegio INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  direccion VARCHAR(255)
);

CREATE TABLE Equipos (
  id_equipo INT PRIMARY KEY AUTO_INCREMENT,
  deporte VARCHAR(100),
  integrantes INT,
  id_colegio INT,
  FOREIGN KEY (id_colegio) REFERENCES Colegios(id_colegio)
);

CREATE TABLE Jugadores (
  dni INT PRIMARY KEY,
  id_equipo INT,
  mail VARCHAR(255),
  FOREIGN KEY (id_equipo) REFERENCES Equipos(id_equipo)
);

CREATE TABLE DT (
  dni INT PRIMARY KEY,
  name VARCHAR(100),
  surname VARCHAR(100),
  telefono INT,
  id_equipo INT,
  mail VARCHAR(255),
  FOREIGN KEY (id_equipo) REFERENCES Equipos(id_equipo)
);

CREATE TABLE Partidos (
  id_partido INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATETIME,
  equipo_local INT,
  equipo_visitante INT,
  resultado VARCHAR(100),
  cancha VARCHAR(100),
  FOREIGN KEY (equipo_local) REFERENCES Equipos(id_equipo),
  FOREIGN KEY (equipo_visitante) REFERENCES Equipos(id_equipo)
);