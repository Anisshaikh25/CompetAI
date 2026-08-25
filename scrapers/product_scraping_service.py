from scrapers.product_scraper import ProductScraper
from scrapers.product_snapshot_scraper import ProductSnapshotScraper

from services.product_service import ProductService
from services.pro_snapshot_service import SnapshotService
from services.job_run_service import JobRunService

from enums import JobType


class ProductScrapingService:

    def __init__(self, db):

        # Services
        self.product_service = ProductService(db)
        self.snapshot_service = SnapshotService(db)
        self.job_service = JobRunService(db)

        # Scrapers
        self.product_scraper = ProductScraper()
        self.snapshot_scraper = ProductSnapshotScraper()

    # --------------------------------------------------
    # Scrape Complete Product Workflow
    # --------------------------------------------------

    def scrape_product(
        self,
        competitor_id: int,
        url: str,
        triggered_by: str = "manual"
    ):
        """
        Complete product scraping workflow:

        1. Start job
        2. Scrape product data
        3. Save or get product
        4. Scrape product snapshot
        5. Save product snapshot
        6. Mark job successful

        If any error occurs:
        7. Mark job as failed
        """

        job = self.job_service.start_job(
            job_type=JobType.PRODUCT_SCRAPER,
            triggered_by=triggered_by
        )

        try:

            # ------------------------------------------
            # Scrape Main Product Data
            # ------------------------------------------

            product_data = (
                self.product_scraper.scrape_product(url)
            )

            # ------------------------------------------
            # Save / Get Product
            # ------------------------------------------

            product = (
                self.product_service.process_product(
                    competitor_id=competitor_id,
                    product_data=product_data
                )
            )

            # ------------------------------------------
            # Scrape Product Snapshot
            # ------------------------------------------

            snapshot_data = (
                self.snapshot_scraper.scrape_snapshot(url)
            )

            # ------------------------------------------
            # Save Product Snapshot
            # ------------------------------------------

            snapshot = (
                self.snapshot_service.create_snapshot(
                    product_id=product.id,
                    snapshot_data=snapshot_data
                )
            )

            # ------------------------------------------
            # Mark Job Successful
            # ------------------------------------------

            self.job_service.complete_job(
                job=job,
                products_scraped=1
            )

            return {
                "job": job,
                "product": product,
                "snapshot": snapshot
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
            # Close Scraper Sessions
            # ------------------------------------------

            self.product_scraper.close()
            self.snapshot_scraper.close()