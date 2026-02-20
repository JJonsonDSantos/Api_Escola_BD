from sqlalchemy.orm import Session
from app import models

def criar_estudante(db: Session, estudante):
    db_estudante = models.Estudante(**estudante.model_dump())
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

def listar_estudantes(db: Session):
    return db.query(models.Estudante).all()

def buscar_estudante(db: Session, estudante_id: int):
    return db.query(models.Estudante).filter(
        models.Estudante.id == estudante_id
    ).first()

def criar_matricula(db: Session, matricula):
    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

def atualizar_estudante(db: Session, estudante_id: int, dados):
    estudante = buscar_estudante(db, estudante_id)

    if not estudante:
        return None

    for campo, valor in dados.model_dump().items():
        setattr(estudante, campo, valor)

    db.commit()
    db.refresh(estudante)
    return estudante

def deletar_estudante(db: Session, estudante_id: int):
    estudante = buscar_estudante(db, estudante_id)

    if not estudante:
        return None

    db.delete(estudante)
    db.commit()
    return estudante

def buscar_matricula(db: Session, matricula_id: int):
    return db.query(models.Matricula).filter(
        models.Matricula.id == matricula_id
    ).first()

def atualizar_matricula(db: Session, matricula_id: int, dados):
    matricula = buscar_matricula(db, matricula_id)

    if not matricula:
        return None

    matricula.nome_disciplina = dados.nome_disciplina
    db.commit()
    db.refresh(matricula)
    return matricula

def deletar_matricula(db: Session, matricula_id: int):
    matricula = buscar_matricula(db, matricula_id)

    if not matricula:
        return None

    db.delete(matricula)
    db.commit()
    return matricula


