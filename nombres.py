from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class person(BaseModel):
    id:int
    Nombre: str
    Edad:int
    estatura: float
    Ocupacion: str
    


persons_list= [person(id=1,Nombre="Laura", Edad="33", estatura="1.60", Ocupacion="Profesora"),
            person(id=2,Nombre="Marlenne", Edad="19", estatura="1.67", Ocupacion="Veterinaria"),
            person(id=3,Nombre="Jesus", Edad="22", estatura="1.70", Ocupacion="Streamer"),
            person(id=4,Nombre="Rodrigo", Edad="21", estatura="1.66", Ocupacion="Conductor"),
            person(id=5,Nombre="Jordan", Edad="23", estatura="1.60", Ocupacion="Abogado"),
            person(id=6,Nombre="Aldo", Edad="17", estatura="1.68", Ocupacion="Arquitecto")]

@router.get("/persons/")
async def imprimir():
    return (persons_list)