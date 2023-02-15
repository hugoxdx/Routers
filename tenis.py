from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class tenis(BaseModel):
    id: int
    modelo: str
    marca: str
    color: str
    precio:int


tenis_list= [tenis(id=1,marca="Nike",modelo="Air Max",color="Blanco", precio="1800"),
             tenis(id=2,marca="Adidas",modelo="Grand Court",color="blanco", precio="1200"),
             tenis(id=3,marca="Puma", modelo="X-Ray",color="Rojo", precio="2100"),
             tenis(id=4,marca="Under Armour", modelo="Charged",color="Gris", precio="1200")
        
           ]

@router.get("/tenis/")
async def imprimir():
    return (tenis_list)