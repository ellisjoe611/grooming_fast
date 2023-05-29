from sqlalchemy.orm import Session

from .model import CountryTable
from .schema import Country


def get_countries(db_session: Session) -> list[Country]:
    return db_session.query(CountryTable).all()
