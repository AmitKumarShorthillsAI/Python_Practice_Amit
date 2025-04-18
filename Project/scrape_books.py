import requests
from bs4 import BeautifulSoup
import pandas as pd

class BookScraper:
    def __init__(self, base_url, start_url, max_pages=5):
        self.base_url = base_url
        self.start_url = start_url
        self.max_pages = max_pages
        self.books_data = []

    def get_soup(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_book_info(self, book):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        availability = book.find('p', class_='instock availability').text.strip()
        return {
            "Title": title,
            "Price": price,
            "Availability": availability
        }

    def get_next_page_url(self, soup):
        next_btn = soup.find('li', class_='next')
        if next_btn:
            next_page_rel = next_btn.a['href']
            return self.base_url + "catalogue/" + next_page_rel
        return None

    def scrape_books(self):
        current_url = self.start_url
        page_count = 0

        while current_url and page_count < self.max_pages:
            print(f"Scraping Page {page_count + 1}: {current_url}")
            soup = self.get_soup(current_url)
            if not soup:
                break

            books = soup.find_all('article', class_='product_pod')
            for book in books:
                book_info = self.extract_book_info(book)
                self.books_data.append(book_info)

            current_url = self.get_next_page_url(soup)
            page_count += 1

    def save_to_csv(self, filename='books.csv'):
        df = pd.DataFrame(self.books_data)
        df.to_csv(filename, index=False)
        print(f"\Scraping complete! Data saved to {filename}")

    def run(self):
        self.scrape_books()
        self.save_to_csv()

if __name__ == "__main__":
    BASE_URL = "http://books.toscrape.com/"
    START_URL = "http://books.toscrape.com/catalogue/page-1.html"

    scraper = BookScraper(base_url=BASE_URL, start_url=START_URL, max_pages=5)
    scraper.run()
