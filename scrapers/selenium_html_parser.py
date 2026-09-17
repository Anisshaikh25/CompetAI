from bs4 import BeautifulSoup


class SeleniumHTMLParser:

    def __init__(self, html: str):
        self.soup = BeautifulSoup(
            html,
            "html.parser"
        )

    def find_text(
        self,
        selector: str
    ) -> str | None:

        element = self.soup.select_one(
            selector
        )

        if not element:
            return None

        return element.get_text(
            strip=True
        )

    def find_all_text(
        self,
        selector: str
    ) -> list[str]:

        elements = self.soup.select(
            selector
        )

        return [
            element.get_text(strip=True)
            for element in elements
        ]

    def find_attribute(
        self,
        selector: str,
        attribute: str
    ) -> str | None:

        element = self.soup.select_one(
            selector
        )

        if not element:
            return None

        return element.get(attribute)