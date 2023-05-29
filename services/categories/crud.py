from sqlalchemy.orm import Session

from .model import CategoryMstTable, CategoryDtlTable
from .schema import CategoryMst as CategoryMstSchema, CategoryDtl as CategoryDtlSchema


def get_category_mst(db_session: Session) -> list[CategoryMstSchema]:
    query = db_session.query(CategoryMstTable)
    return query.all()


def get_category_dtl(db_session: Session, cat_mst_cd: str) -> list[CategoryDtlSchema]:
    query = db_session.query(CategoryDtlTable).filter(
        CategoryDtlTable.cat_mst_cd == cat_mst_cd
    )
    return query.all()
