from typing import List

from pydantic import BaseModel


class SArticleAdd(BaseModel):
    tags: List[str]
    title: str
    text: str

    class Config:
        orm_mode = True

class SArticle(SArticleAdd):
    id: int


class Article(BaseModel):
    id: int
    tags: List[str]
    title: str
    text: str

    class Config:
        orm_mode = True


class SArticleId(BaseModel):
    ok: bool = True
    article_id: int

class ArticleSearchRequest(BaseModel):
    tags: List[str]