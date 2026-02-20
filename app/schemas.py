from pydantic import BaseModel
from typing import List

class MatriculaBase(BaseModel):
    nome_disciplina: str

class MatriculaCreate(MatriculaBase):
    estudante_id: int

class MatriculaResponse(MatriculaBase):
    id: int

    class Config:
        from_attributes = True


class EstudanteBase(BaseModel):
    nome: str
    idade: int

class EstudanteCreate(EstudanteBase):
    pass

class EstudanteResponse(EstudanteBase):
    id: int
    matriculas: List[MatriculaResponse] = []

    class Config:
        from_attributes = True
