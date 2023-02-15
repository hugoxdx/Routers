from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class soda(BaseModel):
    id: int
    marca: str
    litros: float
    precio:int

soda_list= [soda(id=1,marca="Coca Cola",litros="3", precio="45"),
            soda(id=2,marca="Fanta",litros="2.5", precio="39"),
            soda(id=3,marca="Pepsi",litros="1", precio="19"),
            soda(id=4,marca="Squirt",litros="3", precio="42"),
            soda(id=5,marca="Mundet",litros="2.7", precio="30")        
           ]

@router.get("/sodas/")
async def imprimir():
    return (soda_list)