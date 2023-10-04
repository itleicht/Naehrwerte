import sqlite3

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('naehrwerte.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute('''CREATE TABLE naehrwerte
                 (id INTEGER PRIMARY KEY,
                  lebensmittel TEXT,
                  hersteller TEXT,
                  kalorien REAL,
                  eiweiss REAL,
                  fett REAL,
                  kohlenhydrate REAL,
                  davon_zucker REAL,
                  ballaststoffe REAL,
                  alkohol REAL)''')

# Daten in die Tabelle einfügen
cursor.execute("INSERT INTO naehrwerte (lebensmittel, hersteller, kalorien, eiweiss, fett, kohlenhydrate, davon_zucker, ballaststoffe, alkohol) VALUES ('Wert 1', 'Wert 2', 123, 10.5, 5.2, 20.3, 15.5, 3.2, 0.0)")
cursor.execute("INSERT INTO naehrwerte (lebensmittel, hersteller, kalorien, eiweiss, fett, kohlenhydrate, davon_zucker, ballaststoffe, alkohol) VALUES ('Wert 4', 'Wert 5', 456, 15.2, 8.7, 30.1, 25.0, 4.9, 0.0)")

# Änderungen speichern
conn.commit()

# Verbindung zur Datenbank schließen
conn.close()
