from datetime import datetime
import requests
import csv
import bs4


if __name__ == '__main__':
    with open('amazon_products_urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(url)