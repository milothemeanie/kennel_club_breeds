import sqlite3

DB = "kennel.db"

SELECT_RAW = "SELECT id, breed, temperament_raw FROM breed_raw"
conn = sqlite3.connect(DB)
try:
    rows = conn.cursor().execute(SELECT_RAW).fetchall()
finally:
    conn.close()

INSERT_TEMPERAMENT = "INSERT INTO temperament (breed_raw_id, desc) " \
                     "  VALUES (?, ?)"

conn = sqlite3.connect(DB)
try:
    for row in rows:
        print(row)
        for desc in row[2].split(","):
            conn.execute(INSERT_TEMPERAMENT, (row[0], desc.strip()))
            conn.commit()
finally:
    conn.close()
