from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class earphone(BaseModel):
    id: int
    marca: str
    alambricos: str
    bateria: str
    precio:int


ear_list= [earphone(id=1,marca="Samsung", alambricos="No", bateria="4 horas", precio="1200"),
           earphone(id=1,marca="Xiaomi", alambricos="No", bateria="6 horas", precio="1390"),
           earphone(id=1,marca="Skullcandy", alambricos="Si", bateria="N/A", precio="2300"),
           earphone(id=1,marca="Beats", alambricos="Si", bateria="N/A", precio="4400"),
           earphone(id=1,marca="Bose", alambricos="Si", bateria="N/A", precio="1500"),]

@router.get("/earphones/")
async def imprimir():
    return (ear_list)