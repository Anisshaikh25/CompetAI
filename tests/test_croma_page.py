from selenium.webdriver.common.by import By

from scrapers.selenium_scraper import SeleniumScraper
from scrapers.selenium_html_parser import SeleniumHTMLParser


CROMA_URL = (
    "https://www.croma.com/l/reliable-laptop-0afz00a.html"
)


def main():

    scraper = SeleniumScraper(
        headless=False
    )

    try:
        print("Opening Croma...")

        scraper.open_page(CROMA_URL)

        print("Page opened successfully!")
        print(f"Page title: {scraper.get_title()}")

        print("\nWaiting for page body...")

        scraper.wait_for_element(
            By.TAG_NAME,
            "body"
        )

        print("Page body found!")

        html = scraper.get_html()

        print(
            f"\nRendered HTML length: {len(html)}"
        )

        parser = SeleniumHTMLParser(html)

        # --------------------------------------------------
        # Inspect product-related elements
        # --------------------------------------------------

        print(
            "\nInspecting product-related HTML..."
        )

        for selector in [
            "article",
            "[class*='product']",
            "[class*='Product']",
            "[class*='card']",
            "[class*='Card']",
        ]:

            elements = parser.soup.select(
                selector
            )

            print(
                f"{selector} -> "
                f"{len(elements)} elements"
            )

        # --------------------------------------------------
        # Inspect links
        # --------------------------------------------------

        print("\nInspecting links...")

        links = parser.soup.find_all(
            "a",
            href=True
        )

        print(
            f"Total links found: {len(links)}"
        )

        print("\nFirst 30 links:\n")

        for index, link in enumerate(
            links[:30],
            start=1
        ):

            text = link.get_text(
                " ",
                strip=True
            )

            href = link.get("href")

            print(
                f"{index}. "
                f"text={text[:100]}"
            )

            print(
                f"   href={href}"
            )

    except Exception as e:

        print("\nCroma inspection failed!")
        print(f"Error: {e}")

    finally:

        scraper.close()

        print("\nBrowser closed.")


if __name__ == "__main__":
    main()