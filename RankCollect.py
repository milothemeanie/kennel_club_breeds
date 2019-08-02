import sqlite3

DB = "kennel.db"

SELECT_RAW = "SELECT id, breed, popularity_raw FROM breed_raw WHERE popularity_raw IS NOT NULL"
conn = sqlite3.connect(DB)

try:
    rows = conn.cursor().execute(SELECT_RAW).fetchall()
finally:
    conn.close()

UPDATE = "UPDATE breed_raw SET popularity = ? WHERE id = ?"

conn = sqlite3.connect(DB)
try:
    for row in rows:
        print(row)
        p = row[2].split(' ')[1]
        print("parsed popularity ", p)
        conn.execute(UPDATE, (p, row[0]))
        conn.commit()
finally:
    conn.close()
