from database.db import SessionLocal
from database.repositories.competitor_repository import CompetitorRepository

db = SessionLocal()

try:
    repo = CompetitorRepository(db)

    competitor = repo.get_by_name("Dell")

    repo.deactivate_competitor(competitor)

    print(competitor.is_active)
finally:
    db.close()
