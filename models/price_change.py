from sqlalchemy import String, DateTime, ForeignKey, Numeric,Float, Integer, Text, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

from database.db import Base
from datetime import datetime

from enums import PriceChangeType

# ======================================================
# PriceChange Model
# ======================================================
   
class PriceChange(Base):
    __tablename__ = "price_changes"

    id: Mapped[int] = mapped_column(primary_key=True)

    snapshot_id: Mapped[int] = mapped_column(
        ForeignKey("product_snapshots.id"),
        nullable=False,
        index=True
    )

    old_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    new_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    price_difference: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    percentage_change: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    change_type: Mapped[PriceChangeType] = mapped_column(
        SQLEnum(PriceChangeType),
        nullable=False
    )

    detected_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )

    snapshot: Mapped["ProductSnapshot"] = relationship(
        back_populates="price_changes"
    )
