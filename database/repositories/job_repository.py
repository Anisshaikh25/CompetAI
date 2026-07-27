from datetime import datetime

from sqlalchemy import select

from models.jobrun import JobRun
from enums import JobStatus, JobType
from .base_repository import BaseRepository


class JobRunRepository(BaseRepository):

    # --------------------------------------------------
    # Get Job Run by ID
    # --------------------------------------------------

    def get_by_id(self, job_id: int) -> JobRun | None:

        statement = select(JobRun).where(JobRun.id == job_id)

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    # --------------------------------------------------
    # Get All Job Runs
    # --------------------------------------------------

    def get_all(self) -> list[JobRun]:

        statement = (
            select(JobRun)
            .order_by(JobRun.started_at.desc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Get Job Runs by Type
    # --------------------------------------------------

    def get_by_job_type(
        self,
        job_type: JobType
    ) -> list[JobRun]:

        statement = (
            select(JobRun)
            .where(JobRun.job_type == job_type)
            .order_by(JobRun.started_at.desc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Get Job Runs by Status
    # --------------------------------------------------

    def get_by_status(
        self,
        status: JobStatus
    ) -> list[JobRun]:

        statement = (
            select(JobRun)
            .where(JobRun.status == status)
            .order_by(JobRun.started_at.desc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Create Job Run
    # --------------------------------------------------

    def create_job_run(
        self,
        job_type: JobType,
        triggered_by: str = "scheduler"
    ) -> JobRun:

        job = JobRun(
            job_type=job_type,
            triggered_by=triggered_by
        )

        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)

        return job

    # --------------------------------------------------
    # Mark Job as Success
    # --------------------------------------------------

    def mark_success(
        self,
        job: JobRun,
        products_scraped: int = 0,
        blogs_scraped: int = 0,
        documents_indexed: int = 0
    ) -> JobRun:

        finished = datetime.utcnow()

        job.status = JobStatus.SUCCESS
        job.finished_at = finished

        job.products_scraped = products_scraped
        job.blogs_scraped = blogs_scraped
        job.documents_indexed = documents_indexed

        job.duration_seconds = int(
            (finished - job.started_at).total_seconds()
        )

        self.db.commit()
        self.db.refresh(job)

        return job

    # --------------------------------------------------
    # Mark Job as Failed
    # --------------------------------------------------

    def mark_failed(
        self,
        job: JobRun,
        error_message: str
    ) -> JobRun:

        finished = datetime.utcnow()

        job.status = JobStatus.FAILED
        job.finished_at = finished
        job.error_message = error_message

        job.duration_seconds = int(
            (finished - job.started_at).total_seconds()
        )

        self.db.commit()
        self.db.refresh(job)

        return job

    # --------------------------------------------------
    # Delete Job Run
    # --------------------------------------------------

    def delete_job_run(
        self,
        job: JobRun
    ) -> None:

        self.db.delete(job)
        self.db.commit()