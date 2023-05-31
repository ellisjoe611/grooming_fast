from sqlalchemy.orm import Session

from models.model_country import CountryTable
from schemas.schema_country import Country


def get_countries(db_session: Session) -> list[Country]:
    return db_session.query(CountryTable).all()
