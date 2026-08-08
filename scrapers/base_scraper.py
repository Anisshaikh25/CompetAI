import requests


class BaseScraper:

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/151.0.0.0 Safari/537.36"
            )
        })

    def fetch_page(self, url: str) -> str:

        response = self.session.get(
            url,
            timeout=15
        )

        response.raise_for_status()

        return response.text

    def close(self):
        self.session.close()