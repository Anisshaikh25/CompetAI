from sqlalchemy import String, Boolean, DateTime, ForeignKey, Numeric,Float, Integer, Text, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

from database.db import Base
from datetime import datetime

from enums import JobStatus, JobType

class JobRun(Base):
    __tablename__ = "job_runs"

    id: Mapped[int] = mapped_column(primary_key=True)

    job_type: Mapped[JobType] = mapped_column(
        SQLEnum(JobType),
        nullable=False
    )

    status: Mapped[JobStatus] = mapped_column(
        SQLEnum(JobStatus),
        default=JobStatus.RUNNING,
        nullable=False
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime
    )

    products_scraped: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    blogs_scraped: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    documents_indexed: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    error_message: Mapped[str | None] = mapped_column(
        Text
    )

    duration_seconds: Mapped[int | None] = mapped_column(
        Integer
    )