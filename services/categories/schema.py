from pydantic import BaseModel


class CategoryMstBase(BaseModel):
    cat_mst_cd: str
    cat_mst_nm: str


class CategoryDtlBase(BaseModel):
    cat_mst_cd: str
    cat_dtl_cd: str
    cat_dtl_nm: str


class CategoryMst(CategoryMstBase):
    class Config:
        orm_mode = True


class CategoryDtl(CategoryDtlBase):
    master: CategoryMst

    class Config:
        orm_mode = True
