DROP DATABASE IF EXISTS newchic_analytics;

CREATE DATABASE newchic_analytics;
USE newchic_analytics;

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(500) NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE product_stats (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    original_price DECIMAL(10,2),
    sale_price DECIMAL(10,2),
    discount_rate INT,
    review_count INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE INDEX idx_category
ON products(category_id);

CREATE INDEX idx_product
ON product_stats(product_id);
