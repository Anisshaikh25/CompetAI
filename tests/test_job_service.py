from database.db import SessionLocal
from services.job_run_service import JobRunService
from enums import JobType


db = SessionLocal()

try:

    job_service = JobRunService(db)

    # --------------------------------------------------
    # Start Job
    # --------------------------------------------------

    job = job_service.start_job(
        job_type=JobType.PRODUCT_SCRAPER,
        triggered_by="manual"
    )

    print("Job started successfully!")
    print("Job ID:", job.id)
    print("Job Type:", job.job_type)
    print("Status:", job.status)

    # --------------------------------------------------
    # Complete Job
    # --------------------------------------------------

    job = job_service.complete_job(
        job=job,
        products_scraped=10,
        blogs_scraped=2,
        documents_indexed=5
    )

    print("\nJob completed successfully!")
    print("Status:", job.status)
    print("Products scraped:", job.products_scraped)
    print("Blogs scraped:", job.blogs_scraped)
    print("Documents indexed:", job.documents_indexed)
    print("Duration:", job.duration_seconds, "seconds")

finally:
    db.close()