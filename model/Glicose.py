from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from model import Base

class Glicose(Base):
    __tablename__ = 'glicose'

    id = Column("pk_glicose", Integer, primary_key=True)
    nome = Column(String(60), unique=False)
    glicose = Column(Float)

    # A data será sempre considerada como o valor padrão para facilitar o registro para aqueles que não estão familiarizados com isso.
    inclusao_data = Column(DateTime, default= datetime.now())

    def __init__(self, nome:str, glicose:float):       
        """
        cria um registro de glicose

        argumens:
            nome: Nome da pessoa
            glicose: valor de glicose medido
            inclusao_data: data em que foi inserido
        """

        self.nome = nome
        self.glicose = glicose