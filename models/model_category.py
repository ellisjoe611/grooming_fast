from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from core.db import Base


class CategoryMstTable(Base):
    __tablename__ = "cat_mst"

    cat_mst_cd = Column(String(length=100), primary_key=True, index=True)
    cat_mst_nm = Column(String(length=100), nullable=False, index=True)

    details = relationship(
        "CategoryDtlTable",
        back_populates="master"
    )


class CategoryDtlTable(Base):
    __tablename__ = "cat_dtl"

    cat_mst_cd = Column(
        String(length=100),
        ForeignKey("cat_mst.cat_mst_cd"),
        primary_key=True,
        index=True
    )
    cat_dtl_cd = Column(String(length=100), primary_key=True, index=True)
    cat_dtl_nm = Column(String(length=100), nullable=False, index=True)

    master = relationship(
        "CategoryMstTable",
        back_populates="details",
        foreign_keys=[cat_mst_cd],
        uselist=False
    )
