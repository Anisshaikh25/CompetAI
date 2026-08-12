from database.repositories.job_repository import JobRunRepository
from enums import JobType, JobStatus

class JobRunService:

    def __init__(self, db):
        self.job_repo = JobRunRepository(db)

    def start_job(
        self,
        job_type: JobType,
        triggered_by: str = "scheduler"
    ):
        return self.job_repo.create_job_run(
            job_type=job_type,
            triggered_by=triggered_by
        )

    def complete_job(
        self,
        job,
        products_scraped=0,
        blogs_scraped=0,
        documents_indexed=0
    ):
        return self.job_repo.mark_success(
            job=job,
            products_scraped=products_scraped,
            blogs_scraped=blogs_scraped,
            documents_indexed=documents_indexed
        )

    def fail_job(self, job, error_message):
        return self.job_repo.mark_failed(
            job=job,
            error_message=error_message
        )

    def get_job(self, job_id):
        return self.job_repo.get_by_id(job_id)

    def get_all_jobs(self):
        return self.job_repo.get_all()