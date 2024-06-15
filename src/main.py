from fastapi import FastAPI
from src.knowledge_base.router import router as router_article

app = FastAPI()

app.include_router(router_article)






