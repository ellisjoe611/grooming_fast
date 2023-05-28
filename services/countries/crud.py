from sqlalchemy.orm import Session

from . import model, schema

def get_countries(db_session: Session) -> list[schema.Country]:
    return db_session.query(model.Country).all()
