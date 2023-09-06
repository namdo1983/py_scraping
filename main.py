import requests
from bs4 import BeautifulSoup
from config import TikiData, CURDIR
from os.path import join
import csv

totals = []


def get_data():
    r = requests.get(TikiData.URL_APPLE_PRODUCT, headers=TikiData.HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def parse_data():
    soup_list = get_data()
    items = soup_list.find_all("div", {"class": "info"})
    # print(items)

    for i in items:
        try:
            product = {
                "Name": i.find("div", {"class": "name"}).text,
                "Price": i.find("div", {"class": "price-discount__price"}).text,
                "Sold Out": i.find("span", {"class": "quantity has-border"}).text.split(
                    " "
                )[-1],
                "Discount Price": i.find(
                    "div", {"class": "price-discount__discount"}
                ).text,
            }
            totals.append(product)

        except:
            pass


def main():
    try:
        parse_data()
    finally:
        with open(join(CURDIR, TikiData.REPORT_CSV), "w", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, TikiData.HEADERS_CSV)
            writer.writeheader()
            writer.writerows(totals)
        print("Done")


if __name__ == "__main__":
    main()
