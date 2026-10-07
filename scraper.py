import requests
from bs4 import BeautifulSoup
import pandas as pd


RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def scrape_books():
    books = []

    for page in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select(".product_pod"):
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text
            availability = book.select_one(".availability").text.strip()

            rating_class = book.select_one(".star-rating")["class"][1]
            rating = RATING_MAP[rating_class]

            product_url = "https://books.toscrape.com/catalogue/" + book.h3.a["href"]

            books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Product URL": product_url
            })

    df = pd.DataFrame(books)
    df.to_csv("books_data.csv", index=False)

    return len(df)
