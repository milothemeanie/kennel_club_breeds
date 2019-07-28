import sqlite3
from collections import defaultdict
from enum import Enum

import requests
from bs4 import BeautifulSoup

URL = "http://www.akc.org/dog-breeds/{}"

ALL_BREEDS = "all-breeds"

DB = '/home/cward/PycharmProjects/kennel_club_breeds/kennel.db'


# Example breed description
# Temperament: Playful, Perky, Smart
# Popularity: Ranks 122 of 193
# Height: 9-12 inches (toy), 12-15 inches (miniature), 15-19 inches (Standard)
# Weight: 6-10 pounds (toy), 10-20 pounds (miniature), 25-35 pounds (standard)
# Life Expectancy: 13-15 years
# Group: Non-Sporting Group

def main():
    try:
        breed_list = retrieve_breed_list()

        for breed_link in breed_list[1:]:
            # first_breed = breed_list[1]
            page = requests.get(breed_link)
            desc = defaultdict(lambda: None)
            desc["breed"] = breed_link.split("/")[-2]

            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                lis = soup.find("ul", {"class": "attribute-list"}).find_all("li")
                for i, li in enumerate(lis):
                    span = li.find_all("span", {"class", "attribute-list__description"})
                    value = span[0].text
                    desc[determine_attr(i, value).name] = value
                insert_breed_raw(desc)

    except Exception as ex:
        print("Failed kennel scrape " + repr(ex))


def retrieve_breed_list():
    page = requests.get(URL.format(ALL_BREEDS))
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        breeds = soup.find("select", {"id": "breed-search"}) \
            .find_all("option", {"value": True})

        return [x['value'] for x in breeds]

    else:
        raise Exception('Failed the request for kennel breed list, request code' + page.status_code)


def determine_attr(i, text):
    if i == 0:
        return Info.temperament
    elif text.startswith("Rank"):
        return Info.popularity
    elif "inches" in text:
        return Info.height
    elif "pounds" in text:
        return Info.weight
    elif text.endswith("years"):
        return Info.expectancy
    else:
        return Info.group


def insert_breed_raw(desc):
    print("inserting ", desc)
    conn = sqlite3.connect(DB)
    try:
        conn.execute("INSERT INTO breed_raw "
                     "  (breed, temperament_raw, popularity_raw, height_raw ,weight_raw,expectancy_raw, group_raw)"
                     "VALUES (:breed, :temperament, :popularity, :height, :weight, :expectancy, :group)", desc)
        conn.commit()
    finally:
        conn.close()


class Info(Enum):
    temperament = 0
    popularity = 1
    height = 2
    weight = 3
    expectancy = 4
    group = 5


if __name__ == '__main__':
    main()
