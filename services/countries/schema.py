from pydantic import BaseModel

class Country(BaseModel):
    nation_cd: str
    nation_nm: str
    phone_cd: str

    class Config:
        orm_mode = True
