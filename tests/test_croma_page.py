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

        print(f"\nRendered HTML length: {len(html)}")

        parser = SeleniumHTMLParser(html)

        print("\nSearching for product links...")

        product_links = []

        for link in parser.soup.find_all("a", href=True):

            href = link.get("href")

            if href and "/p/" in href:

                title = link.get_text(
                    " ",
                    strip=True
                )

                if title:
                    product_links.append({
                        "title": title,
                        "url": href
                    })

        print(
            f"Possible product links found: "
            f"{len(product_links)}"
        )

        print("\nFirst 10 possible products:\n")

        for index, product in enumerate(
            product_links[:10],
            start=1
        ):

            print(f"Product {index}")
            print(f"Title: {product['title']}")
            print(f"URL: {product['url']}")
            print("-" * 70)

    except Exception as e:

        print("\nCroma inspection failed!")
        print(f"Error: {e}")

    finally:

        scraper.close()
        print("\nBrowser closed.")


if __name__ == "__main__":
    main()