import sqlite3
import pandas as pd

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect('naehrwerte.db')

# Cursor-Objekt erstellen
cursor = conn.cursor()

# Daten aus der Tabelle abrufen
cursor.execute('SELECT * FROM naehrwerte')

# Pandas DataFrame erstellen
df = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

# Verbindung zur Datenbank schließen
conn.close()

# DataFrame anzeigen
print(df)
