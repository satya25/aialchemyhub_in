CREATE DATABASE IF NOT EXISTS your_database;

USE your_database;

CREATE TABLE IF NOT EXISTS records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    city VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
