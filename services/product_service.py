from decimal import Decimal

from database.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self, db):
        self.product_repo = ProductRepository(db)

    def process_product(
        self,
        competitor_id: int,
        product_data: dict
    ):

        product = self.product_repo.get_or_create(
            competitor_id=competitor_id,
            product_code=product_data["product_code"],
            name=product_data["name"],
            category=product_data.get("category"),
            current_price=product_data.get("current_price"),
            product_url=product_data.get("product_url"),
        )

        return product