from sqlalchemy import String, Boolean, DateTime, ForeignKey, Numeric,Float, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

from database.db import Base
from datetime import datetime

# ======================================================
# BlogPost Model
# ======================================================

class BlogPost(Base):
    __tablename__ = "blog_posts"

    id: Mapped[int] = mapped_column(primary_key=True)

    competitor_id: Mapped[int] = mapped_column(
        ForeignKey("competitors.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        unique=True
    )

    author: Mapped[str | None] = mapped_column(
        String(150)
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    published_at: Mapped[datetime | None] = mapped_column(
        DateTime
    )

    scraped_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        index=True
    )

    is_processed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    competitor: Mapped["Competitor"] = relationship(
        back_populates="blog_posts"
    )

    knowledge_documents: Mapped[list["KnowledgeDocument"]] = relationship(
        back_populates="blog_post",
        cascade="all, delete-orphan"
    )