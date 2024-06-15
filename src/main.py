from fastapi import FastAPI
from src.knowledge_base_editor.router import router as router_editor
from src.knowledge_base_user.router import router as router_user
from src.calculator.router import router as router_calculator
app = FastAPI()

app.include_router(router_editor)
app.include_router(router_user)
app.include_router(router_calculator)




