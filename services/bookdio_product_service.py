from scrapers.bookdio_scraper import BookdioScraper
from services.product_service import ProductService


class BookdioProductService:

    def __init__(self, db):
        self.db = db
        self.scraper = BookdioScraper()
        self.product_service = ProductService(db)

    def scrape_and_save(self, competitor_id: int):
        """
        Scrape books from Bookdio and create/update
        products in the database.
        """

        books = self.scraper.scrape_books()

        saved_products = []

        for book in books:

            product_data = {
                "name": book["name"],
                "product_code": book["product_code"],
                "product_url": book["product_url"],
                "category": book.get("category"),
                "brand": None,
                "current_price": None,
                "currency": book.get("currency", "INR"),
                "image_url": None,
            }

            product = self.product_service.process_product(
                competitor_id=competitor_id,
                product_data=product_data
            )

            saved_products.append(product)

        return saved_products

    def close(self):
        self.scraper.close()