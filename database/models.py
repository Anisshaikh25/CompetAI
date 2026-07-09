from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database.db import Base
from datetime import datetime


class Competitor(Base):
    __tablename__ = "competitors"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    website: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    products: Mapped[list["Product"]] = relationship(
    back_populates="competitor",
    cascade="all, delete-orphan"
    )

# ======================================================
# Product Model
# ======================================================

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    competitor_id: Mapped[int] = mapped_column(
        ForeignKey("competitors.id"),
        nullable=False,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    product_code: Mapped[str | None] = mapped_column(
        String(100),
        unique=True
    )

    product_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    sku: Mapped[str | None] = mapped_column(
        String(100)
    )

    category: Mapped[str | None] = mapped_column(
        String(100)
    )

    brand: Mapped[str | None] = mapped_column(
        String(100)
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    competitor: Mapped["Competitor"] = relationship(
        back_populates="products"
    )