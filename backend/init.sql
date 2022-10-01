CREATE TABLE IF NOT EXISTS product (
    id SERIAL,
    product_name TEXT NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL,
    product_id TEXT NOT NULL,
    amount INTEGER NOT NULL,
    total_price FLOAT NOT NULL,
    PRIMARY KEY(id)
);

DELETE FROM product;
INSERT INTO product (product_name, price) VALUES
('Chocolate Donut', '2.00'),
('Cherry Pie', '20.00'),
('Poffertjes', '0.25'),
('Croissant', '1.00'),
('Mille-feuille', '15.00'),
('Boxemännercher','1.50');
