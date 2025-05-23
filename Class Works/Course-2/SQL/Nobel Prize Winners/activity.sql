CREATE TABLE IF NOT EXISTS NOBEL_WIN (
    YEAR INTEGER,
    SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATEGORY TEXT
);

INSERT INTO NOBEL_WIN (YEAR, SUBJECT, WINNER, COUNTRY, CATEGORY) VALUES
    (1970, 'PHYSICS', 'HANNES ALFVEN', 'SWEDEN', 'SCIENTIST'),
    (1970, 'PHYSICS', 'LOUIS NEEL', 'FRANCE', 'SCIENTIST'),
    (1971, 'PHYSICS', 'PAUL', 'FRANCE', 'SCIENTIST'),
    (1971, 'CHEMESTRY', 'HAMILTON', 'SWEDEN', 'LINGUIST'),
    (1972, 'LITERATURE', 'BENEARD KELSON', 'GERMANY', 'ECONIMICST'),
    (1972, 'ECONOMICS', 'JOSEPH', 'RUSSIA', 'ECONOMICST'),
    (1973, 'BIOLOGY', 'PHILLIPS', 'USA', 'PRIME MINISTER'),
    (1975, 'PHYSICS', 'PETER', 'CHILLE', 'SCIENTIST'),
    (1980, 'BIOLOGY', 'MARTIN', 'USA', 'PRESIDENT'),
    (1981, 'PHYSIOLOGY', 'HANNAH', 'HUNGARY', 'SCIENTIST');

-- (LETTER)% MEANS NOT SELECTING
SELECT * FROM NOBEL_WIN WHERE SUBJECT NOT LIKE 'P%';