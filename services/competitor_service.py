from database.repositories.competitor_repository import CompetitorRepository


class CompetitorService:

    def __init__(self, db):
        self.competitor_repo = CompetitorRepository(db)

    def create_competitor(
        self,
        name: str,
        website: str,
        category: str | None = None
    ):
        """
        Create a new competitor.
        """

        competitor = self.competitor_repo.create_competitor(
            name=name,
            website=website,
            category=category
        )

        return competitor

    def get_competitor(
        self,
        competitor_id: int
    ):
        """
        Get competitor by ID.
        """

        return self.competitor_repo.get_by_id(
            competitor_id
        )

    def get_or_create_competitor(
        self,
        name: str,
        website: str,
        category: str | None = None
    ):
        """
        Get an existing competitor or create a new one.
        """

        competitor = self.competitor_repo.get_by_name(name)

        if competitor:
            return competitor

        return self.create_competitor(
            name=name,
            website=website,
            category=category
        )

    def update_competitor(
        self,
        competitor,
        name: str | None = None,
        website: str | None = None,
        category: str | None = None
    ):
        """
        Update competitor information.
        """

        return self.competitor_repo.update_competitor(
            competitor=competitor,
            name=name,
            website=website,
            category=category
        )

    def deactivate_competitor(
        self,
        competitor
    ):
        """
        Deactivate a competitor.
        """

        return self.competitor_repo.deactivate_competitor(
            competitor
        )