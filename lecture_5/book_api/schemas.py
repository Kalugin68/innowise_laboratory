from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    """Shared fields for books"""
    title: str
    author: str
    year: Optional[int] = None


class BookCreate(BookBase):
    """Schema for creating a book"""
    pass


class BookUpdate(BaseModel):
    """Schema for updating a book"""
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None


class BookOut(BaseModel):
    """Schema for returning a book"""
    id: int
    title: str
    author: str
    year: Optional[int] = None

    class Config:
        orm_mode = True