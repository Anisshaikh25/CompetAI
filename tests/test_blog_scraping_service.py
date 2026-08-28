from database.db import SessionLocal

from services.competitor_service import CompetitorService
from scrapers.blog_scraping_service import BlogScrapingService


# --------------------------------------------------
# Test HTML
# --------------------------------------------------

blog_html = """
<html>
<body>

    <h1 class="blog-title">
        The Future of AI in E-Commerce
    </h1>

    <span class="author">
        John Smith
    </span>

    <span class="published-date">
        July 24, 2026
    </span>

    <div class="blog-content">
        Artificial intelligence is transforming
        the e-commerce industry.
    </div>

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
        name="Dell Blog Integration Test",
        website="https://example.com",
        category="Technology"
    )

    # --------------------------------------------------
    # Create Blog Scraping Service
    # --------------------------------------------------

    scraping_service = BlogScrapingService(db)

    # --------------------------------------------------
    # Mock Blog Scraper
    # --------------------------------------------------

    scraping_service.blog_scraper.fetch_page = (
        lambda url: blog_html
    )

    # --------------------------------------------------
    # Run Complete Blog Scraping Workflow
    # --------------------------------------------------

    result = scraping_service.scrape_blog(
        competitor_id=competitor.id,
        url="https://example.com/blog/ai-ecommerce",
        triggered_by="integration_test"
    )

    # --------------------------------------------------
    # Print Results
    # --------------------------------------------------

    print("\nComplete Blog Scraping Workflow Successful!\n")

    print("Job:")
    print(f"ID: {result['job'].id}")
    print(f"Status: {result['job'].status}")

    print("\nBlog:")
    print(f"ID: {result['blog'].id}")
    print(f"Title: {result['blog'].title}")
    print(f"Author: {result['blog'].author}")
    print(f"URL: {result['blog'].url}")
    print(f"Published At: {result['blog'].published_at}")


finally:

    db.close()