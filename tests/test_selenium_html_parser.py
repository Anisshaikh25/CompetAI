from selenium.webdriver.common.by import By

from scrapers.selenium_scraper import SeleniumScraper
from scrapers.selenium_html_parser import SeleniumHTMLParser


def main():

    scraper = SeleniumScraper(
        headless=False
    )

    try:

        url = "https://www.bookdio.org/all-books"

        print("Opening website...")
        scraper.open_page(url)

        print("Waiting for book table...")

        scraper.wait_for_element(
            By.CSS_SELECTOR,
            "table"
        )

        html = scraper.get_html()

        print("Rendered HTML received!")
        print(f"HTML length: {len(html)}")

        parser = SeleniumHTMLParser(html)

        print("\nTesting BeautifulSoup parser...")

        titles = parser.find_all_text(
            "table tbody tr td:first-child"
        )

        print(f"Titles found: {len(titles)}")

        print("\nFirst 5 titles:\n")

        for index, title in enumerate(
            titles[:5],
            start=1
        ):
            print(f"{index}. {title}")

    except Exception as e:

        print("\nTest failed!")
        print(f"Error: {e}")

    finally:

        scraper.close()
        print("\nBrowser closed.")


if __name__ == "__main__":
    main()