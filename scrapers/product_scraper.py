from decimal import Decimal

from .base_scraper import BaseScraper
from .parser import HTMLParser


class ProductScraper(BaseScraper):

    def scrape_product(self, url: str) -> dict:

        html = self.fetch_page(url)

        parser = HTMLParser(html)

        product = {
            "name": parser.find_text(".product-name"),

            "product_code": parser.find_text(
                ".product-code"
            ),

            "product_url": url,

            "sku": parser.find_text(
                ".sku"
            ),

            "category": parser.find_text(
                ".category"
            ),

            "brand": parser.find_text(
                ".brand"
            ),

            "current_price": self.parse_price(
                parser.find_text(".price")
            ),

            "currency": "INR",

            "image_url": parser.find_attribute(
                ".product-image",
                "src"
            )
        }

        return product

    # --------------------------------------------------
    # Parse Price
    # --------------------------------------------------

    def parse_price(
        self,
        value: str | None
    ) -> Decimal | None:

        if not value:
            return None

        cleaned = (
            value
            .replace("₹", "")
            .replace(",", "")
            .strip()
        )

        try:
            return Decimal(cleaned)

        except Exception:
            return None