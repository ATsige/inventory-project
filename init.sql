CREATE TABLE IF NOT EXISTS products (
    sku VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) CHECK (price >= 0),
    stock_quantity INTEGER DEFAULT 0 CHECK (stock_quantity >= 0)
);

INSERT INTO products (sku, name, price, stock_quantity) VALUES
('LAP1001', 'Laptop', 899.99, 10),
('MOU1002', 'Wireless Mouse', 24.99, 50),
('KEY1003', 'Keyboard', 39.99, 40),
('MON1004', 'Monitor', 179.99, 20),
('USB1005', 'USB Cable', 9.99, 100),
('HDP1006', 'External Hard Drive', 79.99, 15),
('WEB1007', 'Webcam', 49.99, 25),
('PRI1008', 'Printer Paper', 12.99, 60),
('HEA1009', 'Headset', 59.99, 30),
('LAM1010', 'Desk Lamp', 29.99, 18);