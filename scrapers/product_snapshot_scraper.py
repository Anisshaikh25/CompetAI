from decimal import Decimal

from .base_scraper import BaseScraper
from .parser import HTMLParser


class ProductSnapshotScraper(BaseScraper):

    def scrape_snapshot(self, url: str) -> dict:

        html = self.fetch_page(url)

        parser = HTMLParser(html)

        snapshot = {
            "price": self.parse_price(
                parser.find_text(".price")
            ),

            "currency": "INR",

            "rating": self.parse_float(
                parser.find_text(".rating")
            ),

            "reviews_count": self.parse_int(
                parser.find_text(".reviews-count")
            ),

            "availability": parser.find_text(
                ".availability"
            ),

            "discount_percentage": self.parse_float(
                parser.find_text(".discount")
            ),

            "seller": parser.find_text(
                ".seller"
            )
        }

        return snapshot

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

    # --------------------------------------------------
    # Parse Float
    # --------------------------------------------------

    def parse_float(
        self,
        value: str | None
    ) -> float | None:

        if not value:
            return None

        cleaned = (
            value
            .replace("%", "")
            .replace("/5", "")
            .strip()
        )

        try:
            return float(cleaned)

        except Exception:
            return None

    # --------------------------------------------------
    # Parse Integer
    # --------------------------------------------------

    def parse_int(
        self,
        value: str | None
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

        except Exception:
            return None