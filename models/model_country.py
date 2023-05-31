from sqlalchemy import Column, String

from core.db import Base


class CountryTable(Base):
    __tablename__ = "countries"

    nation_cd = Column(String(length=100), primary_key=True, index=True)
    nation_nm = Column(String(length=100), nullable=False, index=True)
    phone_cd = Column(String(length=10), nullable=False, index=True)
