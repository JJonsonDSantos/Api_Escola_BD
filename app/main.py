from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import estudantes, matriculas


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Escola")
app = FastAPI()

app.include_router(estudantes.router)
app.include_router(matriculas.router)

@app.get("/")
def root():
    return {"mensagem": "API Escola funcionando 🚀"}