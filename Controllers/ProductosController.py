from pydantic import BaseModel
from fastapi import APIRouter


rutas_producto = APIRouter()

productos =[]

class Productos(BaseModel):
    idProducto: int
    nomProducto: str
    precio : float
    existencia : str

    

    ##Ruta Productos
    @rutas_producto.get("/productos")
    async def todos():
        return productos
    
    ##Ruta para crear un producto
    @rutas_producto.post("/productos")
    async def enviar(prod : Productos):
        productos.append(prod)
        return{

         "mensaje":"Producto Agregado",
         "Producto": prod
        }
    
    ##Actualizar producto
    @rutas_producto.put("/productos/{id}")
    async def actualizar(id: int, prod: Productos):
        for i, p in enumerate(productos):
            if p.idProducto == id:
                productos[i] = prod
                return {"mensaje": "Producto Actualizado"}
        return {"mensaje": "Producto no encontrado"}
    
    ##Eliminar producto
    @rutas_producto.delete("/productos/{id}")
    async def eliminar(id: int):
        for i, p in enumerate(productos):
            if p.idProducto == id:
                productos.pop(i)
                return {"mensaje": "Producto eliminado"}
        return {"mensaje": "Producto no encontrado"}
