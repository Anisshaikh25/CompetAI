from scrapers.blog_scraper import BlogScraper

from services.blog_service import BlogService
from services.job_run_service import JobRunService

from enums import JobType


class BlogScrapingService:

    def __init__(self, db):

        # Services
        self.blog_service = BlogService(db)
        self.job_service = JobRunService(db)

        # Scraper
        self.blog_scraper = BlogScraper()

    # --------------------------------------------------
    # Scrape Complete Blog Workflow
    # --------------------------------------------------

    def scrape_blog(
        self,
        competitor_id: int,
        url: str,
        triggered_by: str = "manual"
    ):
        """
        Complete blog scraping workflow:

        1. Start job
        2. Scrape blog data
        3. Process and save blog
        4. Mark job successful

        If any error occurs:
        5. Mark job as failed
        """

        job = self.job_service.start_job(
            job_type=JobType.BLOG_SCRAPER,
            triggered_by=triggered_by
        )

        try:

            # ------------------------------------------
            # Scrape Blog Data
            # ------------------------------------------

            blog_data = self.blog_scraper.scrape_blog(url)

            # ------------------------------------------
            # Save / Get Blog
            # ------------------------------------------

            blog = self.blog_service.process_blog(
                competitor_id=competitor_id,
                blog_data=blog_data
            )

            # ------------------------------------------
            # Mark Job Successful
            # ------------------------------------------

            self.job_service.complete_job(
                job=job,
                blogs_scraped=1
            )

            return {
                "job": job,
                "blog": blog
            }

        except Exception as error:

            # ------------------------------------------
            # Mark Job Failed
            # ------------------------------------------

            self.job_service.fail_job(
                job=job,
                error_message=str(error)
            )

            raise

        finally:

            # ------------------------------------------
            # Close Scraper Session
            # ------------------------------------------

            self.blog_scraper.close()