from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

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

    blog_posts: Mapped[list["BlogPost"]] = relationship(
    back_populates="competitor",
    cascade="all, delete-orphan"
    )
