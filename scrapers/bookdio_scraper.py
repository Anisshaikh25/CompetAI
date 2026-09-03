from decimal import Decimal
from .base_scraper import BaseScraper
from bs4 import BeautifulSoup


class BookdioScraper(BaseScraper):

    BASE_URL = "https://www.bookdio.org"
    BOOKS_URL = "https://www.bookdio.org/all-books"

    def scrape_books(self) -> list[dict]:
        """
        Scrape all books from Bookdio's all-books page.
        """

        html = self.fetch_page(self.BOOKS_URL)

        soup = BeautifulSoup(html, "html.parser")

        books = []

        # Find all table rows
        rows = soup.find_all("tr")

        for row in rows:

            cells = row.find_all("td")

            # Ignore header / incomplete rows
            if len(cells) < 5:
                continue

            # First cell contains book title and URL
            link = cells[0].find("a")

            if not link:
                continue

            title_element = link.find("div")

            if title_element:
                title = title_element.get_text(
                    strip=True
                )
            else:
                title = link.get_text(
                    strip=True
                )

            product_url = link.get("href")

            if not title or not product_url:
                continue

            # Make relative URLs absolute
            if product_url.startswith("/"):
                product_url = self.BASE_URL + product_url

            category = cells[1].get_text(
                strip=True
            )

            author = cells[2].get_text(
                strip=True
            )

            pages = self.parse_int(
                cells[3].get_text(strip=True)
            )

            rating = self.parse_rating(
                cells[4].get_text(strip=True)
            )

            # Generate a stable product code
            product_code = self.generate_product_code(
                product_url
            )

            book = {
                "name": title,
                "product_code": product_code,
                "product_url": product_url,
                "category": category,
                "author": author,
                "pages": pages,
                "rating": rating,
                "currency": "INR",
            }

            books.append(book)

        return books

    def generate_product_code(
        self,
        url: str
    ) -> str:

        """
        Generate a product code from the Bookdio URL.
        """

        slug = url.rstrip("/").split("/")[-1]

        return slug[:100]

    def parse_int(
        self,
        value: str
    ) -> int | None:

        if not value:
            return None

        cleaned = (
            value
            .replace(",", "")
            .strip()
        )

        try:
            return int(cleaned)

        except ValueError:
            return None

    def parse_rating(
        self,
        value: str
    ) -> float | None:

        if not value:
            return None

        cleaned = (
            value
            .replace("★", "")
            .replace("☆", "")
            .replace("/5", "")
            .strip()
        )

        try:
            return float(cleaned)

        except ValueError:
            return None