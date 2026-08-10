from database.repositories.product_snapshot_repository import ProductSnapshotRepository


class SnapshotService:

    def __init__(self, db):
        self.snapshot_repo = ProductSnapshotRepository(db)

    def create_snapshot(
        self,
        product_id: int,
        snapshot_data: dict
    ):
        """
        Create a price/product snapshot from scraped data.
        """

        snapshot = self.snapshot_repo.create_snapshot(
            product_id=product_id,
            price=snapshot_data["price"],
            currency=snapshot_data.get("currency", "INR"),
            rating=snapshot_data.get("rating"),
            reviews_count=snapshot_data.get("reviews_count"),
            availability=snapshot_data.get(
                "availability",
                "In Stock"
            ),
            discount_percentage=snapshot_data.get(
                "discount_percentage"
            ),
            seller=snapshot_data.get("seller"),
        )

        return snapshot