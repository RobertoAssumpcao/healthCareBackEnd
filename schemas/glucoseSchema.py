from pydantic import BaseModel
from datetime import datetime
from typing import List
from model.glucose import Glucose

class GlucoseSchemaRequest(BaseModel):
    """
    Dto class for registering a new glucose record
    """
    name: str = "Name"
    glucose: float = 0.0

class GlucoseSchemaResponse(BaseModel):
    """
    Glucose response
    """
    id: int = 0
    name: str = "Name"
    glucose: float = 0.0
    insertion_date: datetime = None

class GlucoseListSchemaResponse(BaseModel):
    """
    Glucose list response
    """
    glucoses: List[GlucoseSchemaResponse]

def list_glucoses(glucoses: list[Glucose]):
    result = []
    
    for item in glucoses:
        result.append({
            "id": item.id,
            "name": item.name,
            "glucose": item.glucose,
            "insertion_date": item.insertion_date
            })
        
    return {"glucoses": result}