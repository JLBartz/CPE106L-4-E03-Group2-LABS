import sqlite3

# Create in-memory database
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Create tables
cur.executescript("""
CREATE TABLE Renter (
    Renter_ID INTEGER PRIMARY KEY,
    First_Name TEXT,
    Middle_Initial TEXT,
    Last_Name TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Phone TEXT,
    Email TEXT
);

CREATE TABLE Location (
    Location_Num INTEGER PRIMARY KEY,
    Location_Name TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT
);

CREATE TABLE Condo_Unit (
    Condo_ID INTEGER PRIMARY KEY,
    Location_Num INTEGER,
    Unit_Num TEXT,
    Square_Feet INTEGER,
    Bedrooms INTEGER,
    Bathrooms INTEGER,
    Weekly_Rate REAL,
    Owner_Num TEXT,
    FOREIGN KEY (Location_Num) REFERENCES Location(Location_Num)
);

CREATE TABLE Rental_Agreement (
    Agreement_ID INTEGER PRIMARY KEY,
    Renter_ID INTEGER,
    Condo_ID INTEGER,
    Start_Date TEXT,
    End_Date TEXT,
    Weekly_Rate REAL,
    FOREIGN KEY (Renter_ID) REFERENCES Renter(Renter_ID),
    FOREIGN KEY (Condo_ID) REFERENCES Condo_Unit(Condo_ID)
);
""")

# Insert sample renters
cur.execute("INSERT INTO Renter VALUES (1, 'John', 'K', 'Doe', '123 Beach Rd.', 'Miami', 'FL', '33101', '305-555-1234', 'john.doe@example.com')")
cur.execute("INSERT INTO Renter VALUES (2, 'Alice', 'L', 'Smith', '45 Ocean Blvd.', 'Tampa', 'FL', '33606', '813-555-5678', 'alice.smith@example.com')")

# Insert sample locations
cur.execute("INSERT INTO Location VALUES (1, 'Solmaris Ocean', '100 Ocean Ave.', 'Bowton', 'FL', '31313')")
cur.execute("INSERT INTO Location VALUES (2, 'Solmaris Bayside', '405 Bayside Blvd.', 'Glander Bay', 'FL', '31044')")

# Insert sample condo units
cur.execute("INSERT INTO Condo_Unit VALUES (1, 1, '102', 675, 1, 1, 475.00, 'AD057')")
cur.execute("INSERT INTO Condo_Unit VALUES (2, 2, 'A01', 1084, 2, 1, 235.00, 'NO225')")

# Insert rental agreements
cur.execute("INSERT INTO Rental_Agreement VALUES (1, 1, 1, '2025-07-01', '2025-07-08', 475.00)")
cur.execute("INSERT INTO Rental_Agreement VALUES (2, 2, 2, '2025-07-15', '2025-07-22', 235.00)")

print("\nRenter Details:")
cur.execute("SELECT * FROM Renter")
for row in cur.fetchall():
    print(row)

print("\nProperty Details:")
cur.execute("""
SELECT c.Condo_ID, l.Location_Name, l.Address, l.City, l.State, l.Postal_Code,
       c.Unit_Num, c.Square_Feet, c.Bedrooms, c.Bathrooms, c.Weekly_Rate
FROM Condo_Unit c
JOIN Location l ON c.Location_Num = l.Location_Num
""")
for row in cur.fetchall():
    print(row)

print("\nRental Agreements:")
cur.execute("""
SELECT ra.Renter_ID, r.First_Name, r.Middle_Initial, r.Last_Name, r.Address, r.City, r.State, r.Postal_Code, r.Phone,
       ra.Start_Date, ra.End_Date, ra.Weekly_Rate
FROM Rental_Agreement ra
JOIN Renter r ON ra.Renter_ID = r.Renter_ID
""")
for row in cur.fetchall():
    print(row)
