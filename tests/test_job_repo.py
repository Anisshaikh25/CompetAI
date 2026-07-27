from database.db import SessionLocal

from database.repositories.job_repository import JobRunRepository
from enums import JobType

db = SessionLocal()

try:

    job_repo = JobRunRepository(db)

    job = job_repo.create_job_run(
        JobType.PRODUCT_SCRAPER
    )

    print(job)

    job = job_repo.mark_success(
        job,
        products_scraped=25,
        blogs_scraped=8,
        documents_indexed=12
    )

    print(job.status)

finally:
    db.close()