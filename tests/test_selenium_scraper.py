from scrapers.selenium_scraper import SeleniumScraper


def main():

    scraper = SeleniumScraper(headless=True)

    try:
        url = "https://www.bookdio.org/all-books"

        print("Opening website...")
        scraper.open_page(url)

        print("\nPage opened successfully!")

        print("Page title:")
        print(scraper.get_title())

        html = scraper.get_html()

        print("\nRendered HTML length:")
        print(len(html))

        print("\nFirst 500 characters:")
        print(html[:500])

    except Exception as e:

        print("\nSelenium test failed!")
        print(f"Error: {e}")

    finally:
        scraper.close()
        print("\nBrowser closed.")


if __name__ == "__main__":
    main()