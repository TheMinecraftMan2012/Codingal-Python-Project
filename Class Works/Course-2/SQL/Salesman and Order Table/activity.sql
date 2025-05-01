CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Commision REAL
);

INSERT INTO Salesman (Salesman_id, name, city, Commision) VALUES
    ('5001', 'James Hoog', 'New York', 0.15),
    ('5002', 'Nail Knite', 'Paris', 0.13),
    ('5003', 'Pit Alex', 'London', 0.11),
    ('5004', 'Mc Lyon', 'Paris', 0.14),
    ('5005', 'Paul Adam', 'Rome', 0.13),
    ('5006', 'Lauson Hen', 'San Jose', 0.11);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders (
    order_no PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO Orders (order_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
    ('700001', 250.0, '26/04/2025', '25005', '5001'),
    ('700002', 257.24, '27/04/2025', '25006', '5002'),
    ('700011', 141.25, '28/04/2025', '25007', '5003'),
    ('700025', 1000.25, '29/04/2025', '25008', '5004'),
    ('700026', 759.12, '30/04/2025', '25009', '5005'),
    ('700036', 1459.0, '01/05/2025', '25010', '5006');

SELECT * FROM Orders;