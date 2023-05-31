from fastapi import APIRouter, Depends

from core.db import get_db_session
from schemas.schema_country import Country
from crud.crud_country import get_countries

router: APIRouter = APIRouter()


@router.get("/countries", response_model=list[Country])
def get_all_countries(db_session=Depends(get_db_session)):
    countries = get_countries(db_session=db_session)
    return countries
