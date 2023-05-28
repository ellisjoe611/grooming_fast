from fastapi import APIRouter, Depends

from initializations.db import get_db_session
from .schema import CategoryMst, CategoryDtl
from .crud import get_category_mst, get_category_dtl

router: APIRouter = APIRouter()


@router.get("/category", response_model=list[CategoryMst])
def get_categories(db_session=Depends(get_db_session)):
    cat_mst_list = get_category_mst(db_session=db_session)
    return cat_mst_list


@router.get("/category/{cat_mst_cd}", response_model=list[CategoryDtl])
def get_categories(cat_mst_cd: str, db_session=Depends(get_db_session)):
    cat_dtl_list = get_category_dtl(cat_mst_cd=cat_mst_cd, db_session=db_session)
    return cat_dtl_list
