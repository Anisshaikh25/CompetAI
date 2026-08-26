from database.db import SessionLocal

from services.competitor_service import CompetitorService
from scrapers.product_scraping_service import ProductScrapingService


# --------------------------------------------------
# Test HTML for ProductScraper
# --------------------------------------------------

product_html = """
<html>
<body>

    <h1 class="product-name">
        Dell XPS 13
    </h1>

    <span class="product-code">
        XPS13-INTEGRATION-2026
    </span>

    <span class="price">
        ₹1,29,999
    </span>

    <span class="sku">
        XPS13SKU
    </span>

    <span class="category">
        Laptop
    </span>

    <span class="brand">
        Dell
    </span>

    <img
        class="product-image"
        src="https://example.com/xps13.jpg"
    >

</body>
</html>
"""


# --------------------------------------------------
# Test HTML for ProductSnapshotScraper
# --------------------------------------------------

snapshot_html = """
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


# --------------------------------------------------
# Database Session
# --------------------------------------------------

db = SessionLocal()


try:

    # --------------------------------------------------
    # Get or Create Test Competitor
    # --------------------------------------------------

    competitor_service = CompetitorService(db)

    competitor = competitor_service.get_or_create_competitor(
        name="Dell Integration Test",
        website="https://example.com",
        category="Technology"
    )

    # --------------------------------------------------
    # Create Product Scraping Service
    # --------------------------------------------------

    scraping_service = ProductScrapingService(db)

    # --------------------------------------------------
    # Mock Product Scraper
    # --------------------------------------------------

    scraping_service.product_scraper.fetch_page = (
        lambda url: product_html
    )

    # --------------------------------------------------
    # Mock Snapshot Scraper
    # --------------------------------------------------

    scraping_service.snapshot_scraper.fetch_page = (
        lambda url: snapshot_html
    )

    # --------------------------------------------------
    # Run Complete Scraping Workflow
    # --------------------------------------------------

    result = scraping_service.scrape_product(
        competitor_id=competitor.id,
        url="https://example.com/xps13",
        triggered_by="integration_test"
    )

    # --------------------------------------------------
    # Print Results
    # --------------------------------------------------

    print("\nComplete Product Scraping Workflow Successful!\n")

    print("Job:")
    print(
        f"ID: {result['job'].id}"
    )
    print(
        f"Status: {result['job'].status}"
    )

    print("\nProduct:")
    print(
        f"ID: {result['product'].id}"
    )
    print(
        f"Name: {result['product'].name}"
    )
    print(
        f"Price: {result['product'].current_price}"
    )

    print("\nSnapshot:")
    print(
        f"ID: {result['snapshot'].id}"
    )
    print(
        f"Price: {result['snapshot'].price}"
    )
    print(
        f"Rating: {result['snapshot'].rating}"
    )
    print(
        f"Reviews: {result['snapshot'].reviews_count}"
    )


finally:

    db.close()