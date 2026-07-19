from sqlalchemy.orm import Session
from sqlalchemy import select
from models.competitor import Competitor

from .base_repository import BaseRepository


class CompetitorRepository(BaseRepository):
    ## get competitor by name
    def get_by_name(self, name: str) -> Competitor | None:

        statement = select(Competitor).where(
            Competitor.name == name
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()
    
    ## create a new competitor
    
    def create_competitor(
    self,
    name: str,
    website: str,
    category: str
    ) -> Competitor:
        
        competitor = Competitor(
        name=name,
        website=website,
        category=category
        )

        self.db.add(competitor)

        self.db.commit()

        self.db.refresh(competitor)

        return competitor
    
    ## get or create competitor 

    def get_or_create(
    self,
    name: str,
    website: str,
    category: str
    ) -> Competitor:

      competitor = self.get_by_name(name)

      if competitor:
          return competitor

      return self.create_competitor(
          name=name,
          website=website,
          category=category
    )
    
    ## getbyid competitor 

    def get_by_id(self, competitor_id: int) -> Competitor | None:

      statement = select(Competitor).where(
          Competitor.id == competitor_id
      )

      result = self.db.execute(statement)

      return result.scalar_one_or_none()
    
    ## getall competitor 

    def get_all(self) -> list[Competitor]:

      statement = select(Competitor)

      result = self.db.execute(statement)

      return result.scalars().all()
    
    ## update competitor 

    def update_competitor(
    self,
    competitor: Competitor,
    website: str | None = None,
    category: str | None = None,
    is_active: bool | None = None
    ) -> Competitor:

      if website is not None:
          competitor.website = website

      if category is not None:
          competitor.category = category

      if is_active is not None:
          competitor.is_active = is_active

      self.db.commit()

      self.db.refresh(competitor)

      return competitor
    
    ##delete/ deactivate competitor

    def deactivate_competitor(
    self,
    competitor: Competitor
    ) -> Competitor:

      competitor.is_active = False

      self.db.commit()

      self.db.refresh(competitor)

      return competitor