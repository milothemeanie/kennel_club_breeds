import sqlite3
from statistics import median
import re

DB = "kennel.db"

SELECT_RAW = "SELECT id, breed, height_raw FROM breed_raw WHERE height_raw IS NOT NULL"
conn = sqlite3.connect(DB)
try:
    rows = conn.cursor().execute(SELECT_RAW).fetchall()
finally:
    conn.close()

    # INSERT_TEMPERAMENT = "INSERT INTO temperament (breed_raw_id, desc) " \
    #                      "  VALUES (?, ?)"
    #
    # conn = sqlite3.connect(DB)
    # try:
    regex = re.compile(r'^\d{1,3}\.?\d?-\d{1,3}\.?\d?')
    for row in rows:
        print(row[2].split(' '))
        for seg in row[2].split(' '):
            if regex.search(seg):
                print(seg)
                r = seg.split('-')
                min_h = float(r[0])
                max_h = float(r[1])
                median_h = median([min_h, max_h])
                print("min:%s median:%s max:%s" % (min_h, median_h, max_h))

#         for desc in row[2].split(","):
#             conn.execute(INSERT_TEMPERAMENT, (row[0], desc.strip()))
#             conn.commit()
# finally:
#     conn.close()
