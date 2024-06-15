from typing import List

from sqlalchemy import ARRAY, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Model(DeclarativeBase):
    pass

class ArticleOrm(Model):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tags: Mapped[List[str]] = mapped_column(ARRAY(String))
    title: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
