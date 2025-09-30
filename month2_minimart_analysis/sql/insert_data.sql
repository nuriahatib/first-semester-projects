-- SQL script to insert sample data
-- Inserting sample customers
INSERT INTO customers (name, email, phone) VALUES
('John Mwangi', 'john.mwangi@example.com', '0701000001'),
('Grace Achieng', 'grace.achieng@example.com', '0701000002'),
('Peter Otieno', 'peter.otieno@example.com', '0701000003'),
('Mary Wanjiku', 'mary.wanjiku@example.com', '0701000004'),
('Kevin Kiptoo', 'kevin.kiptoo@example.com', '0701000005');

-- Inserting sample products
INSERT INTO products (product_name, price) VALUES
('Milk', 50.00),
('Bread', 30.00),
('Eggs', 120.00),
('Rice', 200.00),
('Sugar', 150.00);

-- Inserting sample orders
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 2, NOW()),   -- John Mwangi buys Milk
(1, 3, 1, NOW()),   -- John Mwangi buys Eggs
(2, 2, 5, NOW()),   -- Grace Achieng buys Bread
(3, 4, 3, NOW()),   -- Peter Otieno buys Rice
(4, 5, 2, NOW());   -- Mary Wanjiku buys Sugar
