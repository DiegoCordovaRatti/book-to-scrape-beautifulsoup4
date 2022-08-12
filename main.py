#books to scrape
import requests
from bs4 import BeautifulSoup
import re
import csv

page = requests.get('https://books.toscrape.com/catalogue/page-1.html')
soup = BeautifulSoup(page.text, 'html.parser')

book_catalogue = []

def turn_to_csv(book_list):
    book_info = ["Image-link", "Title", "Price"]
    with open ("Book_catalogue.csv", "w") as book_file:
        writer = csv.DictWriter(book_file, fieldnames=book_info)
        writer.writeheader()
        writer.writerows(book_list)

books = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
for book in books:
    image_link = book.find(class_='thumbnail')['src']
    title = book.find("h3").find("a")['title']
    price_string = book.find(class_="price_color").text
    price_numbers = re.sub('[^0-9\.]','', price_string)
    price = float(price_numbers)
    book_catalogue.append({"Image-link": image_link, "Title": title, "Price": "£"+str(price)})


turn_to_csv(book_catalogue)