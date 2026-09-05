from scrapers.bookdio_scraper import BookdioScraper


def main():

    scraper = BookdioScraper()

    try:
        print("Starting Bookdio scraper...")

        books = scraper.scrape_books()

        print("\nScraping completed!")
        print(f"Total books scraped: {len(books)}")

        print("\nFirst 5 books:\n")

        for index, book in enumerate(books[:5], start=1):

            print(f"Book {index}")
            print(f"Name: {book['name']}")
            print(f"Product Code: {book['product_code']}")
            print(f"URL: {book['product_url']}")
            print(f"Category: {book['category']}")
            print(f"Author: {book['author']}")
            print(f"Pages: {book['pages']}")
            print(f"Rating: {book['rating']}")
            print("-" * 50)

    except Exception as e:

        print("\nScraping failed!")
        print(f"Error: {e}")

    finally:

        scraper.close()


if __name__ == "__main__":
    main()