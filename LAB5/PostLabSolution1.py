import sqlite3

# Connect to SQLite (simulate)
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Create tables
cur.execute('''
CREATE TABLE Participant (
    Participant_ID TEXT PRIMARY KEY,
    Last_Name TEXT,
    First_Name TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Phone TEXT,
    DOB TEXT
)
''')

cur.execute('''
CREATE TABLE Adventure_Class (
    Class_ID TEXT PRIMARY KEY,
    Description TEXT,
    Max_People INTEGER,
    Fee REAL
)
''')

cur.execute('''
CREATE TABLE Enrollment (
    Enrollment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Participant_ID TEXT,
    Class_ID TEXT,
    Class_Date TEXT,
    FOREIGN KEY (Participant_ID) REFERENCES Participant(Participant_ID),
    FOREIGN KEY (Class_ID) REFERENCES Adventure_Class(Class_ID)
)
''')

#Participant and their enrolled classes
query = '''
SELECT p.Participant_ID, p.Last_Name, p.First_Name, 
       ac.Class_ID, ac.Description, e.Class_Date
FROM Participant p
JOIN Enrollment e ON p.Participant_ID = e.Participant_ID
JOIN Adventure_Class ac ON e.Class_ID = ac.Class_ID
'''
cur.execute(query)
for row in cur.fetchall():
    print(row)

#Class and its participants
query = '''
SELECT ac.Class_Date, ac.Class_ID, ac.Description,
       p.Participant_ID, p.Last_Name, p.First_Name
FROM Adventure_Class ac
JOIN Enrollment e ON ac.Class_ID = e.Class_ID
JOIN Participant p ON e.Participant_ID = p.Participant_ID
'''
cur.execute(query)
for row in cur.fetchall():
    print(row)

conn.close()