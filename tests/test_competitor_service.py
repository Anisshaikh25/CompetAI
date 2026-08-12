from database.db import SessionLocal
from services.competitor_service import CompetitorService


db = SessionLocal()

try:

    competitor_service = CompetitorService(db)

    competitor = competitor_service.get_or_create_competitor(
        name="Apple",
        website="https://www.apple.com",
        category="Technology"
    )

    print("Competitor processed successfully!")
    print("ID:", competitor.id)
    print("Name:", competitor.name)
    print("Website:", competitor.website)
    print("Category:", competitor.category)
    print("Active:", competitor.is_active)

finally:
    db.close()