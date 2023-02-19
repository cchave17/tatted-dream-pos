DROP DATABASE IF EXISTS tatted_dream;
CREATE DATABASE tatted_dream;

use tatted_dream;

CREATE TABLE customers (
  customers_id INT AUTO_INCREMENT NOT NULL,
  Name VARCHAR(255) Default NULL,
  Email VARCHAR(255) Default NULL,
  Phone VARCHAR(255) Default NULL,
  Gender ENUM('Male', 'Female') Default NULL,
  Photo_ID VARCHAR(255) Default NULL,
  Signature BLOB Default NULL,
  PRIMARY KEY (customers_id)
);

CREATE TABLE Tattoos (
  tattoo_id INT AUTO_INCREMENT NOT NULL,
  customer_id INT DEFAULT NULL,
  description VARCHAR(255) DEFAULT NULL,
  photo BLOB DEFAULT NULL,
  signature BLOB DEFAULT NULL,
  cost DECIMAL(10, 2) DEFAULT NULL,
  PRIMARY KEY (tattoo_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customers_id)
);

CREATE TABLE Sessions (
  session_id INT AUTO_INCREMENT NOT NULL,
  tattoo_id INT DEFAULT NULL,
  artist VARCHAR(255) DEFAULT NULL,
  percentage DECIMAL(5, 2) DEFAULT NULL,
  session_cost DECIMAL(10, 2) DEFAULT NULL,
  tip DECIMAL(10, 2) DEFAULT NULL,
  session_date DATE DEFAULT NULL,
  PRIMARY KEY (session_id),
  FOREIGN KEY (tattoo_id) REFERENCES Tattoos(tattoo_id)
);

CREATE TABLE Artists (
  artist_id INT AUTO_INCREMENT NOT NULL,
  name VARCHAR(255) DEFAULT NULL,
  email VARCHAR(255) DEFAULT NULL,
  phone VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (artist_id)
);