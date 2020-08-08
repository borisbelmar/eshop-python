DROP DATABASE IF EXISTS eshop;

CREATE DATABASE eshop;
USE eshop;

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(60) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE brands (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(60) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(60) NOT NULL,
    description TEXT,
    price DOUBLE NOT NULL,
    id_category INT,
    id_brand INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (id_category) REFERENCES categories (id),
    FOREIGN KEY (id_brand) REFERENCES brands (id)
);

INSERT INTO categories (name) VALUES
    ('Chocolate'),
    ('Coffee'),
    ('Cookies'),
    ('Snacks');

INSERT INTO brands (name) VALUES
    ('Rococo'),
    ('Juan Valdez'),
    ('Great Value');

INSERT INTO products (name, description, price, id_category, id_brand) VALUES
    ('Sea Salt Organic', 'Milk chocolate thins', 8000, 1, 1),
    ('Café Nariño 500g', 'Soft coffee from Colombia', 16000, 2, 2);

