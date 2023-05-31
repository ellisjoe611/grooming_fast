from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from core.db import Base

class ItemTable(Base):
    __tablename__ = "items"

    item_cd = Column(Integer, primary_key=True, autoincrement=True, index=True)
    item_nm = Column(String(length=255), nullable=False, index=True)
    region_cd = Column(String(length=50), nullable=False, index=True)
    nation_cd = Column(String(length=10), ForeignKey("countries.nation_cd"), index=True)
    cat_mst_cd = Column(String(length=100), ForeignKey("cat_dtl.cat_mst_cd"), index=True)
    cat_dtl_cd = Column(String(length=100), ForeignKey("cat_dtl.cat_dtl_cd"), index=True)
    company_nm = Column(String(length=100), nullable=True, index=True)
    imported_from = Column(String(length=100), ForeignKey("countries.nation_cd"), index=True)
    quantity = Column(Integer, nullable=False, default=0, index=True)
    is_banned = Column(Boolean, nullable=False, default=False, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(), index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), index=True)
