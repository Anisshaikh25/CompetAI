from scrapers.selenium_scraper import SeleniumScraper
from selenium.webdriver.common.by import By


def main():

    scraper = SeleniumScraper(headless=False)

    try:
        url = "https://www.bookdio.org/all-books"

        print("Opening website...")
        scraper.open_page(url)

        print("\nPage opened successfully!")
        print(f"Page title: {scraper.get_title()}")

        print("\nFinding book rows...")

        rows = scraper.driver.find_elements(
            By.CSS_SELECTOR,
            "table tbody tr"
        )

        print(f"Rows found: {len(rows)}")

        print("\nFirst 5 books:\n")

        for index, row in enumerate(rows[:5], start=1):

            cells = row.find_elements(
                By.TAG_NAME,
                "td"
            )

            if len(cells) < 5:
                continue

            title = cells[0].text.strip()
            category = cells[1].text.strip()
            author = cells[2].text.strip()
            pages = cells[3].text.strip()
            rating = cells[4].text.strip()

            print(f"Book {index}")
            print(f"Title: {title}")
            print(f"Category: {category}")
            print(f"Author: {author}")
            print(f"Pages: {pages}")
            print(f"Rating: {rating}")
            print("-" * 50)

    except Exception as e:

        print("\nSelenium test failed!")
        print(f"Error: {e}")

    finally:
        scraper.close()
        print("\nBrowser closed.")


if __name__ == "__main__":
    main()