from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer)

    matriculas = relationship(
        "Matricula",
        back_populates="estudante",
        cascade="all, delete"
    )

class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)
    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    nome_disciplina = Column(String(100), nullable=False)

    estudante = relationship("Estudante", back_populates="matriculas")
