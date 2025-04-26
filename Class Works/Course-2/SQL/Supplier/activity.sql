CREATE TABLE supplier1 (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier1 (SNO, SNAME, STATUS, CITY) VALUES
    ('S1', 'Smith', 20, 'London'),
    ('S2', 'Jones', 20, 'Paris'),
    ('S3', 'Blake', 20, 'Paris'),
    ('S4', 'Clarke', 20, 'London'),
    ('S5', 'Adams', 20, 'Athens');

SELECT * FROM supplier1;