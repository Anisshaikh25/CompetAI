from database.db import SessionLocal
from database.repositories.product_repository import ProductRepository
from database.repositories.competitor_repository import CompetitorRepository

db = SessionLocal()

try:
    competitor_repo = CompetitorRepository(db)
    product_repo = ProductRepository(db)

    # Get or create a competitor first
    competitor = competitor_repo.get_or_create(
        name="Dell",
        website="https://www.dell.com",
        category="Laptop"
    )

    # Create a product
    product = product_repo.create_product(
        competitor_id=competitor.id,
        product_code="DELL002",
        name="Dell Inspiron 15",
        category="Laptop",
        current_price=59999,
        currency="INR",
        product_url="https://www.dell.com/inspiron15"
    )

    print(product)

finally:
    db.close()