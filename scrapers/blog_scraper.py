from datetime import datetime

from .base_scraper import BaseScraper
from .parser import HTMLParser


class BlogScraper(BaseScraper):

    def scrape_blog(self, url: str) -> dict:

        html = self.fetch_page(url)

        parser = HTMLParser(html)

        blog = {
            "title": parser.find_text(
                ".blog-title"
            ),

            "url": url,

            "author": parser.find_text(
                ".author"
            ),

            "content": parser.find_text(
                ".blog-content"
            ),

            "published_at": self.parse_date(
                parser.find_text(
                    ".published-date"
                )
            )
        }

        return blog

    # --------------------------------------------------
    # Parse Published Date
    # --------------------------------------------------

    def parse_date(
        self,
        value: str | None
    ) -> datetime | None:

        if not value:
            return None

        formats = [
            "%Y-%m-%d",
            "%Y-%m-%d %H:%M:%S",
            "%d-%m-%Y",
            "%B %d, %Y",
            "%b %d, %Y"
        ]

        for date_format in formats:

            try:
                return datetime.strptime(
                    value.strip(),
                    date_format
                )

            except ValueError:
                continue

        return None