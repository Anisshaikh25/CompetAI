from scrapers.product_scraper import ProductScraper


html = """
<html>
<head>
    <title>Dell XPS 13</title>
</head>

<body>

    <h1 class="product-name">
        Dell XPS 13
    </h1>

    <span class="product-code">
        XPS13-2026
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


scraper = ProductScraper()

# Prevent real internet request.
# We provide our own test HTML.
scraper.fetch_page = lambda url: html

try:

    product = scraper.scrape_product(
        "https://example.com/xps13"
    )

    print("Scraped Product:")
    print(product)

finally:
    scraper.close()