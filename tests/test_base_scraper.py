from scrapers.base_scraper import BaseScraper

print("TEST STARTED")

scraper = BaseScraper()

try:
    print("Scraper created")

    html = scraper.fetch_page("https://example.com")

    print("Page fetched successfully!")
    print("HTML length:", len(html))

except Exception as e:
    print("ERROR:", e)

finally:
    scraper.close()
    print("TEST FINISHED")