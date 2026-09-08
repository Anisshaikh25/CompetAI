from database.db import SessionLocal
from services.bookdio_product_service import BookdioProductService


def main():

    db = SessionLocal()

    service = BookdioProductService(db)

    try:
        print("Starting Bookdio product integration...")

        products = service.scrape_and_save(
            competitor_id=7
        )

        print("\nIntegration completed successfully!")
        print(f"Total products saved: {len(products)}")

        print("\nFirst 5 products:\n")

        for index, product in enumerate(products[:5], start=1):

            print(f"Product {index}")
            print(f"ID: {product.id}")
            print(f"Name: {product.name}")
            print(f"Product Code: {product.product_code}")
            print(f"URL: {product.product_url}")
            print(f"Category: {product.category}")
            print(f"Current Price: {product.current_price}")
            print("-" * 50)

    except Exception as e:

        print("\nIntegration failed!")
        print(f"Error: {e}")

        db.rollback()

    finally:
        service.close()
        db.close()


if __name__ == "__main__":
    main()