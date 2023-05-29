from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from initializations.db import Base


class CategoryMst(Base):
    __tablename__ = "cat_mst"
    cat_mst_cd = Column(String(length=100), primary_key=True, index=True)
    cat_mst_nm = Column(String(length=100), nullable=False, index=True)

    detail = relationship("CategoryDtl", back_populates="master")


class CategoryDtl(Base):
    __tablename__ = "cat_dtl"
    cat_mst_cd = Column(String(length=100), ForeignKey(
        "cat_mst.cat_mst_cd"), primary_key=True, index=True)
    cat_dtl_cd = Column(String(length=100), primary_key=True, index=True)
    cat_dtl_nm = Column(String(length=100), nullable=False, index=True)

    master = relationship("CategoryMst", back_populates="detail")
