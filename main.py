from fastapi import FastAPI 
from Controllers.ProductosController import rutas_producto

sena = FastAPI()

#EndPoint
@sena.get("/")
def inicio():
    return "La app esta en Linea"


sena.include_router(rutas_producto)
