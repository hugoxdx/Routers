from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class dog(BaseModel):
    id: int
    raza: str
    color: str
    tamanio: str
    precio:int


dogs_list= [dog(id=1,raza="Boxer",color="cafe",tamanio="Grande", precio="1200"),
            dog(id=2,raza="Chihuahua",color="cafe claro",tamanio="pequeño", precio="1800"),
            dog(id=3,raza="Pastor Aleman",color="cafe y negro",tamanio="Grande", precio="2200"),
            dog(id=4,raza="Pitbull",color="gris",tamanio="mediano", precio="3200"),
            dog(id=5,raza="Boxer",color="cafe",tamanio="Grande", precio="1800"),
                     
           ]

@router.get("/dogs/")
async def imprimir():
    return (dogs_list)