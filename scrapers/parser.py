from bs4 import BeautifulSoup


class HTMLParser:

    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")

    def get_title(self) -> str | None:
        return self.soup.title.get_text(strip=True) if self.soup.title else None

    def get_text(self) -> str:
        return self.soup.get_text(" ", strip=True)

    def find_text(self, selector: str) -> str | None:
        element = self.soup.select_one(selector)

        if element:
            return element.get_text(" ", strip=True)

        return None

    def find_attribute(
        self,
        selector: str,
        attribute: str
    ) -> str | None:

        element = self.soup.select_one(selector)

        if element:
            return element.get(attribute)

        return None