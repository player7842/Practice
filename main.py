from fastapi import FastAPI 

sena = FastAPI()

#EndPoint
@sena.get("/")
def inicio():
    return "La app esta en Linea"



