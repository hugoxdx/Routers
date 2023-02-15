from fastapi import FastAPI
from routers import routers_5, routers2_5, autos, celulares, nombres, earphones, tenis,dogs,tvs,sodas

app= FastAPI()

app.include_router(routers_5.router)
app.include_router(routers2_5.router)
app.include_router(autos.router)
app.include_router(celulares.router)
app.include_router(nombres.router)
app.include_router(earphones.router)
app.include_router(tenis.router)
app.include_router(dogs.router)
app.include_router(tvs.router)
app.include_router(sodas.router)

@app.get("/")

async def imprimir():
    return "Hola estudiantes"