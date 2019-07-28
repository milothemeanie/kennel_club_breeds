import requests
from bs4 import BeautifulSoup

URL = "http://www.akc.org/dog-breeds/{}"

ALL_BREEDS = "all-breeds"


def main():
    try:
        breed_list = retrieve_breed_list()

        for breed_link in breed_list:
            print(breed_link)

        first_breed = breed_list[1]
        page = requests.get(first_breed)
        desc = dict()
        desc["breed"] = first_breed.split("/")[-2]

        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            lis = soup.find("ul", {"class": "attribute-list"}).find_all("li")
            for li in lis:
                span = li.find_all("span", {"class", "attribute-list__description"})
                print(span[0].text)


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


if __name__ == '__main__':
    main()
