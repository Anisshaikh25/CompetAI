from decimal import Decimal

from database.db import SessionLocal
from database.repositories.product_repository import ProductRepository
from services.pro_snapshot_service import SnapshotService


db = SessionLocal()

try:

    product_repo = ProductRepository(db)

    product = product_repo.get_by_product_code(
        "DELL003"
    )

    if not product:
        print("Product DELL003 not found.")
        exit()

    snapshot_service = SnapshotService(db)

    snapshot_data = {
        "price": Decimal("58999.00"),
        "currency": "INR",
        "rating": 4.5,
        "reviews_count": 125,
        "availability": "In Stock",
        "discount_percentage": 8.5,
        "seller": "Dell India"
    }

    snapshot = snapshot_service.create_snapshot(
        product_id=product.id,
        snapshot_data=snapshot_data
    )

    print("Snapshot created successfully!")
    print("Snapshot ID:", snapshot.id)
    print("Product ID:", snapshot.product_id)
    print("Price:", snapshot.price)
    print("Rating:", snapshot.rating)
    print("Reviews:", snapshot.reviews_count)
    print("Availability:", snapshot.availability)
    print("Discount:", snapshot.discount_percentage)
    print("Seller:", snapshot.seller)

finally:
    db.close()