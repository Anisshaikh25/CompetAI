from sqlalchemy import String, Boolean, DateTime, ForeignKey, Numeric,Float, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

from database.db import Base
from datetime import datetime

# ======================================================
# Productsnapshot Model
# ======================================================

class ProductSnapshot(Base):
    __tablename__ = "product_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
        index=True
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR"
    )

    rating: Mapped[float | None] = mapped_column(
        Float
    )

    reviews_count: Mapped[int | None] = mapped_column(
        Integer
    )

    availability: Mapped[str] = mapped_column(
        String(30),
        default="In Stock"
    )

    discount_percentage: Mapped[float | None] = mapped_column(
        Float
    )

    seller: Mapped[str | None] = mapped_column(
        String(100)
    )

    scraped_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )

    product: Mapped["Product"] = relationship(
        back_populates="snapshots"
    )

    price_changes: Mapped[list["PriceChange"]] = relationship(
    back_populates="snapshot",
    cascade="all, delete-orphan"
    )
