from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.knowledge_base_editor.schemas import Article, ArticleSearchRequest, SArticleAdd
from src.models import ArticleOrm


router = APIRouter(
    prefix="/knowledge-base/edit",
    tags=["Editor Knowledge Base"],
)

@router.post("/create-article", response_model=Article)
async def add_article(article: SArticleAdd, session: AsyncSession = Depends(get_async_session)):
    article_orm = ArticleOrm(**article.dict())
    session.add(article_orm)
    await session.commit()
    await session.refresh(article_orm)
    # article_id = await ArticleRepository.add_one(article)
    return article_orm


@router.delete("/delete-article/{article_id}", response_model=Article)
async def delete_article(article_id: int , session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ArticleOrm).where(ArticleOrm.id == article_id))
    article = result.scalar_one_or_none()
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    await session.delete(article)
    await session.commit()
    return article

