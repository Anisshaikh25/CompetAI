from decimal import Decimal

from sqlalchemy import select

from models.product import Product
from .base_repository import BaseRepository


class ProductRepository(BaseRepository):

    def get_by_id(self, product_id: int) -> Product | None:
        statement = select(Product).where(Product.id == product_id)
        result = self.db.execute(statement)
        return result.scalar_one_or_none()

    def get_by_product_code(self, product_code: str) -> Product | None:
        statement = select(Product).where(Product.product_code == product_code)
        result = self.db.execute(statement)
        return result.scalar_one_or_none()

    def get_by_competitor(self, competitor_id: int) -> list[Product]:
        statement = select(Product).where(Product.competitor_id == competitor_id)
        result = self.db.execute(statement)
        return result.scalars().all()

    def get_all(self) -> list[Product]:
        statement = select(Product)
        result = self.db.execute(statement)
        return result.scalars().all()

    def create_product(
        self,
        competitor_id: int,
        product_code: str,
        name: str,
        category: str | None = None,
        brand: str | None = None, 
        sku: str | None = None,
        image_url: str | None = None,
        current_price: Decimal | None = None,
        currency: str = "INR",
        product_url: str | None = None,
    ) -> Product:

        product = Product(
            competitor_id=competitor_id,
            product_code=product_code,
            name=name,
            category=category,
            brand=brand,
            sku=sku,
            image_url=image_url,
            current_price=current_price,
            currency=currency,
            product_url=product_url,
        )

        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_or_create(
        self,
        competitor_id: int,
        product_code: str,
        name: str,
        category: str | None = None,
        brand: str | None = None, 
        sku: str | None = None,
        image_url: str | None = None,
        current_price: Decimal | None = None,
        currency: str = "INR",
        product_url: str | None = None,
    ) -> Product:

        product = self.get_by_product_code(product_code)

        if product:
            return product

        return self.create_product(
            competitor_id=competitor_id,
            product_code=product_code,
            name=name,
            category=category,
            brand=brand,
            sku=sku,
            image_url=image_url,
            current_price=current_price,
            currency=currency,
            product_url=product_url,
        )

    def update_product(
        self,
        product: Product,
        name: str | None = None,
        category: str | None = None,
        current_price: Decimal | None = None,
        currency: str | None = None,
        product_url: str | None = None,
    ) -> Product:

        if name is not None:
            product.name = name

        if category is not None:
            product.category = category

        if current_price is not None:
            product.current_price = current_price

        if currency is not None:
            product.currency = currency

        if product_url is not None:
            product.product_url = product_url

        self.db.commit()
        self.db.refresh(product)
        return product

    def update_current_price(
        self,
        product: Product,
        current_price: Decimal
    ) -> Product:

        product.current_price = current_price

        self.db.commit()
        self.db.refresh(product)
        return product

    def deactivate_product(self, product: Product) -> Product:
        product.is_active = False

        self.db.commit()
        self.db.refresh(product)
        return product