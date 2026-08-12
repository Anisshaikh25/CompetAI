from database.repositories.competitor_repository import CompetitorRepository


class CompetitorService:

    def __init__(self, db):
        self.competitor_repo = CompetitorRepository(db)

    # --------------------------------------------------
    # Create Competitor
    # --------------------------------------------------

    def create_competitor(
        self,
        name: str,
        website: str,
        category: str | None = None
    ):

        return self.competitor_repo.create_competitor(
            name=name,
            website=website,
            category=category
        )

    # --------------------------------------------------
    # Get or Create Competitor
    # --------------------------------------------------

    def get_or_create_competitor(
        self,
        name: str,
        website: str,
        category: str | None = None
    ):

        competitor = self.competitor_repo.get_by_name(name)

        if competitor:
            return competitor

        return self.competitor_repo.create_competitor(
            name=name,
            website=website,
            category=category
        )

    # --------------------------------------------------
    # Get Competitor by ID
    # --------------------------------------------------

    def get_competitor(
        self,
        competitor_id: int
    ):

        return self.competitor_repo.get_by_id(
            competitor_id
        )

    # --------------------------------------------------
    # Update Competitor
    # --------------------------------------------------

    def update_competitor(
        self,
        competitor,
        name: str | None = None,
        website: str | None = None,
        category: str | None = None
    ):

        return self.competitor_repo.update_competitor(
            competitor=competitor,
            name=name,
            website=website,
            category=category
        )

    # --------------------------------------------------
    # Deactivate Competitor
    # --------------------------------------------------

    def deactivate_competitor(
        self,
        competitor
    ):

        return self.competitor_repo.deactivate_competitor(
            competitor
        )