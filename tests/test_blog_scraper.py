from scrapers.blog_scraper import BlogScraper


html = """
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


scraper = BlogScraper()

scraper.fetch_page = lambda url: html

try:

    blog = scraper.scrape_blog(
        "https://example.com/blog/ai-ecommerce"
    )

    print("Scraped Blog:")
    print(blog)

finally:
    scraper.close()