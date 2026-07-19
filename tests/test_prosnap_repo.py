from database.db import SessionLocal

from database.repositories.competitor_repository import CompetitorRepository
from database.repositories.product_repository import ProductRepository
from database.repositories.product_snapshot_repository import ProductSnapshotRepository

db = SessionLocal()

try:

    competitor_repo = CompetitorRepository(db)
    product_repo = ProductRepository(db)
    snapshot_repo = ProductSnapshotRepository(db)

    competitor = competitor_repo.get_or_create(
        name="Dell",
        website="https://www.dell.com",
        category="Laptop"
    )

    product = product_repo.get_or_create(
        competitor_id=competitor.id,
        product_code="DELL001",
        name="Dell Inspiron 15",
        category="Laptop",
        product_url="https://www.dell.com",
        current_price=59999,
        currency="INR"
    )

    snapshot = snapshot_repo.create_snapshot(
        product_id=product.id,
        price=59999,
        currency="INR",
        availability="In Stock",
        rating=4.6,
        reviews_count=150,
        discount_percentage=10,
        seller="Dell Store"
    )

    print(snapshot)

finally:
    db.close()