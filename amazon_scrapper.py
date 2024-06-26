from datetime import datetime
import requests
import csv
import bs4


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User_Agent': USER_AGENT,
    'Aceept-Language': 'en-US, en;q=0.5',
}

#get html page
def get_page_html(url):
    res = requests.get(url=url, headers=REQUEST_HEADER)

    return res.content

#get product price
def get_product_price(soup):
    main_price_span = soup.find('span', class_='a-price')
    price_span = main_price_span.findAll('span')
    for span in price_span:
        price = span.text.strip().replace(",", "")
        print(price)
        

#extract product info
def extract_product_info(url):
    product_info = {}
    print(f"Scrapping Url : {url}")
    html = get_page_html(url=url)
    soup = bs4.BeautifulSoup(html, "lxml")
    product_info['price'] = get_product_price(soup)
    #print(product_info)


if __name__ == '__main__':
    with open('amazon_products_urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))