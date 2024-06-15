from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.knowledge_base.schemas import Article, ArticleSearchRequest
from src.models import ArticleOrm


router = APIRouter(
    prefix="/knowledge-base",
    tags=["Articles"],
)

@router.post("/create-article", response_model=Article)
async def add_article(article: Article, session: AsyncSession = Depends(get_async_session)):
    article_orm = ArticleOrm(**article.dict())
    session.add(article_orm)
    await session.commit()
    await session.refresh(article_orm)
    # article_id = await ArticleRepository.add_one(article)
    return article_orm

@router.get("", response_model=List[Article])
async def get_articles(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ArticleOrm))
    articles = result.scalars().all()
    return articles

@router.get("/{article_id}", response_model=Article)
async def get_article(article_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ArticleOrm).where(ArticleOrm.id == article_id))
    article = result.scalar_one_or_none()
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.post("/search/", response_model=List[Article])
async def search_articles_by_tags(request: ArticleSearchRequest, session: AsyncSession = Depends(get_async_session)):
    tags = request.tags
    if not tags:
        raise HTTPException(status_code=400, detail="Tags must be provided for search")
    query = select(ArticleOrm).filter(func.array_to_string(ArticleOrm.tags, ',').contains(','.join(tags)))
    result = await session.execute(query)
    articles = result.scalars().all()
    return articles