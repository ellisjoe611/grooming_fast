from sqlalchemy.orm import Session

from . import model, schema


def get_category_mst(db_session: Session) -> list[schema.CategoryMst]:
    return db_session.query(model.CategoryMst).all()


def get_category_dtl(db_session: Session, cat_mst_cd: str) -> list[schema.CategoryDtl]:
    return db_session.query(model.CategoryDtl).filter(model.CategoryDtl.cat_mst_cd == cat_mst_cd).all()
