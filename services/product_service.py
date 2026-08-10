from database.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self, db):
        self.product_repo = ProductRepository(db)

    def process_product(
        self,
        competitor_id: int,
        product_data: dict
    ):
        """
        Process scraped product data and save it
        using ProductRepository.
        """

        product = self.product_repo.get_or_create(
            competitor_id=competitor_id,
            product_code=product_data["product_code"],
            name=product_data["name"],
            product_url=product_data["product_url"],
            sku=product_data.get("sku"),
            category=product_data.get("category"),
            brand=product_data.get("brand"),
            current_price=product_data.get("current_price"),
            currency=product_data.get("currency", "INR"),
            image_url=product_data.get("image_url"),
        )

        return product