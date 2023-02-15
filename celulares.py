from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class phone(BaseModel):
    id:int
    Marca: str
    Modelo:str
    Color:str


phone_list= [phone(id=1,Marca="Samsung", Modelo="A52", Color="Rojo"),
             phone(id=2,Marca="Huawei", Modelo="P40", Color="Azul"),
             phone(id=3,Marca="Xiaomi", Modelo="POCO X5", Color="Negro"),
             phone(id=4,Marca="Motorola", Modelo="Edge 8",  Color="Amarillo"),
             phone(id=5,Marca="Oppo", Modelo="Reno 5", Color="Blanco"),
             phone(id=6,Marca="Realme", Modelo="10 Pro", Color="Morado"),
             phone(id=7,Marca="Honor", Modelo="X8", Color="Verde"),
             phone(id=8,Marca="Zte", Modelo="Blade 5", Color="Gris")

            ]

@router.get("/phones/")
async def imprimir():
    return (phone_list)