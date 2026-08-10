from decimal import Decimal

from sqlalchemy import select

from models.product import Product
from .base_repository import BaseRepository


class ProductRepository(BaseRepository):

    def get_by_id(self, product_id: int) -> Product | None:
        statement = select(Product).where(
            Product.id == product_id
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    def get_by_product_code(
        self,
        product_code: str
    ) -> Product | None:

        statement = select(Product).where(
            Product.product_code == product_code
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    def get_by_competitor(
        self,
        competitor_id: int
    ) -> list[Product]:

        statement = select(Product).where(
            Product.competitor_id == competitor_id
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    def get_all(self) -> list[Product]:

        statement = select(Product)

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Create Product
    # --------------------------------------------------

    def create_product(
        self,
        competitor_id: int,
        product_code: str,
        name: str,
        product_url: str,
        sku: str | None = None,
        category: str | None = None,
        brand: str | None = None,
        current_price: Decimal | None = None,
        currency: str = "INR",
        image_url: str | None = None,
    ) -> Product:

        product = Product(
            competitor_id=competitor_id,
            product_code=product_code,
            name=name,
            product_url=product_url,
            sku=sku,
            category=category,
            brand=brand,
            current_price=current_price,
            currency=currency,
            image_url=image_url,
        )

        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)

        return product

    # --------------------------------------------------
    # Get or Create
    # --------------------------------------------------

    def get_or_create(
        self,
        competitor_id: int,
        product_code: str,
        name: str,
        product_url: str,
        sku: str | None = None,
        category: str | None = None,
        brand: str | None = None,
        current_price: Decimal | None = None,
        currency: str = "INR",
        image_url: str | None = None,
    ) -> Product:

        product = self.get_by_product_code(
            product_code
        )

        if product:
            return product

        return self.create_product(
            competitor_id=competitor_id,
            product_code=product_code,
            name=name,
            product_url=product_url,
            sku=sku,
            category=category,
            brand=brand,
            current_price=current_price,
            currency=currency,
            image_url=image_url,
        )

    # --------------------------------------------------
    # Update Product
    # --------------------------------------------------

    def update_product(
        self,
        product: Product,
        name: str | None = None,
        product_url: str | None = None,
        sku: str | None = None,
        category: str | None = None,
        brand: str | None = None,
        current_price: Decimal | None = None,
        currency: str | None = None,
        image_url: str | None = None,
    ) -> Product:

        if name is not None:
            product.name = name

        if product_url is not None:
            product.product_url = product_url

        if sku is not None:
            product.sku = sku

        if category is not None:
            product.category = category

        if brand is not None:
            product.brand = brand

        if current_price is not None:
            product.current_price = current_price

        if currency is not None:
            product.currency = currency

        if image_url is not None:
            product.image_url = image_url

        self.db.commit()
        self.db.refresh(product)

        return product

    # --------------------------------------------------
    # Update Current Price
    # --------------------------------------------------

    def update_current_price(
        self,
        product: Product,
        current_price: Decimal
    ) -> Product:

        product.current_price = current_price

        self.db.commit()
        self.db.refresh(product)

        return product

    # --------------------------------------------------
    # Deactivate Product
    # --------------------------------------------------

    def deactivate_product(
        self,
        product: Product
    ) -> Product:

        product.is_active = False

        self.db.commit()
        self.db.refresh(product)

        return product