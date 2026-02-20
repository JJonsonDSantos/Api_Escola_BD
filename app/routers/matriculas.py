from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.database import SessionLocal


router = APIRouter(prefix="/matriculas", tags=["Matriculas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MatriculaResponse)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    estudante = db.query(models.Estudante).filter(
        models.Estudante.id == matricula.estudante_id
    ).first()

    if not estudante:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")

    return crud.criar_matricula(db, matricula)

@router.put("/{matricula_id}", response_model=schemas.MatriculaResponse)
def atualizar_matricula(
    matricula_id: int,
    matricula: schemas.MatriculaBase,
    db: Session = Depends(get_db)
):
    atualizada = crud.atualizar_matricula(db, matricula_id, matricula)

    if not atualizada:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")

    return atualizada

@router.delete("/{matricula_id}")
def deletar_matricula(matricula_id: int, db: Session = Depends(get_db)):
    deletada = crud.deletar_matricula(db, matricula_id)

    if not deletada:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")

    return {"mensagem": "Matrícula removida com sucesso"}


