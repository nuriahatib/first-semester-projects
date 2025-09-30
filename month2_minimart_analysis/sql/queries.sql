-- SQL queries for retrieving insights
-- Retrieving all orders made by a specific customer
SELECT o.order_id, c.name, p.product_name, o.quantity, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE c.name = 'Alice Johnson';

-- Getting total number of orders
SELECT COUNT(*) AS total_orders FROM orders;

-- Calculating total revenue
SELECT SUM(p.price * o.quantity) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id;

-- INNER JOIN: order details with customer + product names
SELECT o.order_id, c.name, p.product_name, o.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;

-- LEFT JOIN: all products and any related orders
SELECT p.product_name, o.order_id, o.quantity
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id;
