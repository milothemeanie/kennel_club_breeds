import sqlite3

conn = sqlite3.connect('/home/cward/PycharmProjects/kennel_club_breeds/kennel.db')

create = "CREATE TABLE breed_raw (" \
         "id INTEGER PRIMARY KEY AUTOINCREMENT ," \
         "breed TEXT NOT NULL," \
         "temperament_raw TEXT NULL," \
         "popularity_raw TEXT NULL, " \
         "height_raw TEXT NULL," \
         "weight_raw TEXT NULL," \
         "expectancy_raw TEXT NULL," \
         "group_raw TEXT NULL)"

CREATE_TEMPERAMENT = "CREATE TABLE temperament " \
                     "(" \
                     "  id INTEGER PRIMARY KEY AUTOINCREMENT," \
                     "  breed_raw_id INTEGER NOT NULL," \
                     "  desc TEXT NOT NULL" \
                     ")"

conn.execute(create)

# class Info(Enum):
#     temperament = 0
#     popularity = 1
#     height = 2
#     weight = 3
#     expectancy = 4
#     group = 5


# Temperament: Playful, Perky, Smart
# Popularity: Ranks 122 of 193
# Height: 9-12 inches (toy), 12-15 inches (miniature), 15-19 inches (Standard)
# Weight: 6-10 pounds (toy), 10-20 pounds (miniature), 25-35 pounds (standard)
# Life Expectancy: 13-15 years
# Group: Non-Sporting Group
