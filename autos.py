from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class auto(BaseModel):
    id:int
    Marca: str
    Modelo:str
    Anio:int
    Color:str


autos_list= [auto(id=1,Marca="Ford", Modelo="Lobo", Anio="2022", Color="Rojo"),
             auto(id=2,Marca="VolksWagen", Modelo="Tiguan", Anio="2021", Color="Azul"),
             auto(id=3,Marca="Toyota", Modelo="Hilux", Anio="2020", Color="Negro"),
             auto(id=4,Marca="Seat", Modelo="Ibiza", Anio="2019", Color="Amarillo"),
             auto(id=5,Marca="Chevrolet", Modelo="Aveo", Anio="2019", Color="Blanco"),
             auto(id=6,Marca="Dodge", Modelo="Ram", Anio="2022", Color="Morado"),
             auto(id=7,Marca="Mazda", Modelo="A3", Anio="2018", Color="Verde"),
             auto(id=8,Marca="Honda", Modelo="Civic", Anio="2022", Color="Gris")

            ]

@router.get("/autos/")
async def imprimir():
    return (autos_list)