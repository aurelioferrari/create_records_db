import sqlite3
import pandas as pd

conn = sqlite3.connect("Path to db")

cursor = conn.cursor()

df = pd.read_excel("path to excel file", header=None)


i = 0

while i < len(df):
    cliente = df.iloc[i].tolist()
    cursor.execute(
        """INSERT INTO Clientes (Nome, Email, Estado)
        VALUES (?, ?, ?)
        """, (f"{cliente[0]}", f"{cliente[1]}", f"{cliente[2]}")
    )

    
    i += 1
conn.commit()
conn.close()