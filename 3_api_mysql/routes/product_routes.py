from fastapi import APIRouter
from controllers import product_controller
from models.product_model import *

# solo importamos APIRouter porque este fichero ya nos encontramos en la ruta /products, aqui tengo que montar todas las subrutas a partir de ese elemento.

router = APIRouter()

################## READ ######################
# obtener producto por id http://localhost:8000/products/ 

@router.get('/{product_id}', status_code= 200)
async def get_products_by_id(product_id: str):
    #llama al controlador a la funcion obtener_productos por id -->>> RECORDAR pasar id a int
    return await product_controller.obtener_producto_by_id(int(product_id))

## STATUS 
@router.get('/filter/status', status_code= 200)
async def get_products_by_price(product_status: int):
    return await product_controller.obtener_productos_by_status(product_status)

## PRECIO ok  # obtener producto por precioss http://localhost:8000/products/filter/precio?pricemin=20&pricemax=70
@router.get('/filter/precio', status_code= 200)
async def get_products_by_price(pricemin: int,pricemax: int):
    return await product_controller.obtener_productos_by_price(pricemin,pricemax)

## TITULO
@router.get('/filter/title', status_code= 200)
async def get_products_by_price(in_title: str):
    return await product_controller.obtener_productos_by_title(in_title)




################## CREATE ######################

## POST ok
@router.post('/register', status_code= 201)
async def register(product: productCreate):
    return await product_controller.registrar(product)


################## DELETE ######################

@router.delete('/{product_id}', status_code= 200)
async def delete_product_by_id(product_id: str):
    return await product_controller.borrar_producto_by_id(int(product_id))


################## UPDATE ######################
@router.put('/{product_id}', status_code= 200)
async def update_product_by_id(product_id: str, product: product):
    return await product_controller.actualizar_producto_by_id(int(product_id), product)