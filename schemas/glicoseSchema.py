from pydantic import BaseModel
from datetime import datetime
from typing import List
from model.Glicose import Glicose

class GlicoseSchemaRequest(BaseModel):
    """
    Classe Dto para registrar um novo registro de glicose
    """
    nome: str = "Name"
    glicose: float = 0.0

class GlicoseSchemaResponse(BaseModel):
    """
    Glicose response
    """
    id: int = 0
    nome: str = "Name"
    glicose: float = 0.0
    inclusao_data: datetime = None

class GlicoseListSchemaResponse(BaseModel):
    """
    Glicose list response
    """
    glicoses: List[GlicoseSchemaResponse]

class GlicoseSchemaRemove(BaseModel):
    """
    Glicose remover response
    """
    id: int = 0

def list_glicoses(glicoses: list[Glicose]):
    result = []
    
    for item in glicoses:
        result.append({
            "id": item.id,
            "nome": item.nome,
            "glicose": item.glicose,
            "inclusao_data": item.inclusao_data
            })
        
    return {"glicoses": result}