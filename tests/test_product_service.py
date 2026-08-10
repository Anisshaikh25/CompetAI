from database.db import SessionLocal
from database.repositories.competitor_repository import CompetitorRepository
from services.product_service import ProductService


db = SessionLocal()

try:

    competitor_repo = CompetitorRepository(db)

    competitor = competitor_repo.get_by_name("Dell")

    if not competitor:
        print("Competitor Dell not found.")
        exit()

    product_service = ProductService(db)

    product_data = {
        "product_code": "DELL004",
        "name": "Dell Inspiron 15 Service Test",
        "product_url": "https://example.com/dell-inspiron-15",
        "sku": "INS15-003",
        "category": "Laptop",
        "brand": "Dell",
        "current_price": 59999,
        "currency": "INR",
        "image_url": "https://example.com/dell.jpg"
    }

    product = product_service.process_product(
        competitor_id=competitor.id,
        product_data=product_data
    )

    print("Product processed successfully!")
    print("ID:", product.id)
    print("Name:", product.name)
    print("Product Code:", product.product_code)
    print("Brand:", product.brand)
    print("Price:", product.current_price)

finally:
    db.close()