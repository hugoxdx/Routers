from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class tv(BaseModel):
    id: int
    marca: str
    pulgadas: int
    precio:int

tvs_list= [tv(id=1,marca="Samsung",pulgadas="49", precio="4500"),
           tv(id=1,marca="TCL",pulgadas="108", precio="8800"),
           tv(id=1,marca="LG",pulgadas="39", precio="14000"),
           tv(id=1,marca="Panasonic",pulgadas="50", precio="9900"),
           tv(id=1,marca="Daevo",pulgadas="90", precio="2900"),

                     
           ]

@router.get("/tvs/")
async def imprimir():
    return (tvs_list)