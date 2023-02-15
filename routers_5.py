#en vez de importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter

#En vez de crear fastApi crfeo APIRouter
router= APIRouter()

#instancia de productos
@router.get("/products")
async def products():
    return ["Prducto1", "Producto2", "Prducto3", "Producto4", "Prducto5"]

