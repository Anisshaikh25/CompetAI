from scrapers.product_snapshot_scraper import (
    ProductSnapshotScraper
)


html = """
<html>
<body>

    <span class="price">
        ₹1,29,999
    </span>

    <span class="rating">
        4.5
    </span>

    <span class="reviews-count">
        238
    </span>

    <span class="availability">
        In Stock
    </span>

    <span class="discount">
        10%
    </span>

    <span class="seller">
        Dell India
    </span>

</body>
</html>
"""


scraper = ProductSnapshotScraper()

scraper.fetch_page = lambda url: html

try:

    snapshot = scraper.scrape_snapshot(
        "https://example.com/xps13"
    )

    print("Scraped Snapshot:")
    print(snapshot)

finally:
    scraper.close()