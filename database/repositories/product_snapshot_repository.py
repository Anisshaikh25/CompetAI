from datetime import datetime

from sqlalchemy import select

from database.db import SessionLocal
from models.product_snapshot import ProductSnapshot


class ProductSnapshotRepository:

    def __init__(self, db: SessionLocal):
        self.db = db

    # --------------------------------------------------
    # Get Snapshot by ID
    # --------------------------------------------------

    def get_by_id(
        self,
        snapshot_id: int
    ) -> ProductSnapshot | None:

        statement = select(ProductSnapshot).where(
            ProductSnapshot.id == snapshot_id
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    # --------------------------------------------------
    # Get All Snapshots of a Product
    # --------------------------------------------------

    def get_by_product(
        self,
        product_id: int
    ) -> list[ProductSnapshot]:

        statement = (
            select(ProductSnapshot)
            .where(ProductSnapshot.product_id == product_id)
            .order_by(ProductSnapshot.scraped_at.desc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Get Latest Snapshot
    # --------------------------------------------------

    def get_latest_snapshot(
        self,
        product_id: int
    ) -> ProductSnapshot | None:

        statement = (
            select(ProductSnapshot)
            .where(ProductSnapshot.product_id == product_id)
            .order_by(ProductSnapshot.scraped_at.desc())
            .limit(1)
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    # --------------------------------------------------
    # Create Snapshot
    # --------------------------------------------------

    def create_snapshot(
        self,
        product_id: int,
        price,
        currency: str = "INR",
        availability: str = "In Stock",
        rating: float | None = None,
        reviews_count: int | None = None,
        discount_percentage: float | None = None,
        seller: str | None = None
    ) -> ProductSnapshot:

        snapshot = ProductSnapshot(
            product_id=product_id,
            price=price,
            currency=currency,
            availability=availability,
            rating=rating,
            reviews_count=reviews_count,
            discount_percentage=discount_percentage,
            seller=seller
        )

        self.db.add(snapshot)

        self.db.commit()

        self.db.refresh(snapshot)

        return snapshot

    # --------------------------------------------------
    # Complete Price History
    # --------------------------------------------------

    def get_price_history(
        self,
        product_id: int
    ) -> list[ProductSnapshot]:

        statement = (
            select(ProductSnapshot)
            .where(ProductSnapshot.product_id == product_id)
            .order_by(ProductSnapshot.scraped_at.asc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Get Snapshots Between Dates
    # --------------------------------------------------

    def get_snapshots_between(
        self,
        product_id: int,
        start_date: datetime,
        end_date: datetime
    ) -> list[ProductSnapshot]:

        statement = (
            select(ProductSnapshot)
            .where(
                ProductSnapshot.product_id == product_id,
                ProductSnapshot.scraped_at >= start_date,
                ProductSnapshot.scraped_at <= end_date
            )
            .order_by(ProductSnapshot.scraped_at.asc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Delete Snapshot
    # --------------------------------------------------

    def delete_snapshot(
        self,
        snapshot: ProductSnapshot
    ) -> None:

        self.db.delete(snapshot)

        self.db.commit()