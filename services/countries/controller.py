from fastapi import APIRouter, Depends

from initializations.db import get_db_session
from . import schema, crud

router: APIRouter = APIRouter()


@router.get("/countries", response_model=list[schema.Country])
def get_all_countries(db_session=Depends(get_db_session)):
    countries = crud.get_countries(db_session=db_session)
    return countries
