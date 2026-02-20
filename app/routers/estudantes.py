from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/estudantes", tags=["Estudantes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.EstudanteResponse)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    return crud.criar_estudante(db, estudante)

@router.get("/", response_model=list[schemas.EstudanteResponse])
def listar_estudantes(db: Session = Depends(get_db)):
    return crud.listar_estudantes(db)

@router.get("/{estudante_id}", response_model=schemas.EstudanteResponse)
def buscar_estudante(estudante_id: int, db: Session = Depends(get_db)):
    estudante = crud.buscar_estudante(db, estudante_id)
    if not estudante:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return estudante

@router.put("/{estudante_id}", response_model=schemas.EstudanteResponse)
def atualizar_estudante(
    estudante_id: int,
    estudante: schemas.EstudanteCreate,
    db: Session = Depends(get_db)
):
    atualizado = crud.atualizar_estudante(db, estudante_id, estudante)

    if not atualizado:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")

    return atualizado

@router.delete("/{estudante_id}")
def deletar_estudante(estudante_id: int, db: Session = Depends(get_db)):
    deletado = crud.deletar_estudante(db, estudante_id)

    if not deletado:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")

    return {"mensagem": "Estudante removido com sucesso"}

from app.auth import verificar_token

@router.get("/")
def listar_estudantes(db: Session = Depends(get_db)):
    return crud.listar_estudantes(db)

