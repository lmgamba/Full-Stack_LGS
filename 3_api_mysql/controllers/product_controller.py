import aiomysql as aio
from db.config import *
from fastapi import HTTPException
from models.product_model import *


#AQUI SE CONECTA A LA DATABASE
#################################################
################## READ ######################
async def obtener_producto_by_id(product_id: int):
    try:
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("SELECT * FROM products WHERE id=%s",(product_id,))
            product=await cursor.fetchone()
            return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
        
        
#### obtener productos entre un rango de precios #####

async def obtener_productos_by_price(pricemin: int,pricemax: int):
    
    if pricemin > pricemax:
        raise   HTTPException(status_code=400, detail="El precio min no puede ser mayor al maxima")
    
    try:
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("SELECT * FROM products WHERE products.price BETWEEN %s AND %s ",(pricemin,pricemax))
            res= await cursor.fetchall()
            if len(res) != 0:
                return res
            else:
                raise   HTTPException(status_code=404, detail="No se encontraron productos entre esoss precios")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
        
        
##### obtener productos entre un rango de precioesbuscador ##
async def obtener_productos_by_title(in_title: str):

    try:
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("SELECT * FROM products WHERE products.title LIKE %s ",(f'%{in_title}%',))
            res= await cursor.fetchall()
            if len(res) != 0:
                return res
            else:
                raise   HTTPException(status_code=404, detail="No se encontraron productos con ese titulo")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
 
 ########STATUS############       
async def obtener_productos_by_status(product_status:int):
    try:
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("SELECT * FROM products WHERE status=%s ",(product_status,))
            res= await cursor.fetchall()
            if len(res) != 0:
                return res
            else:
                raise   HTTPException(status_code=404, detail="No se encontraron productos con ese status")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()


#### obtener productos entre un rango de precios #####

async def obtener_productos_by_quantity(quantmin,quantmax):
    
    if quantmin > quantmax:
        raise   HTTPException(status_code=400, detail="La cantidad min no puede ser mayor a la maxima")
    
    try:
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("SELECT * FROM products WHERE products.quantity BETWEEN %s AND %s ",(quantmin,quantmax))
            res= await cursor.fetchall()
            if len(res) != 0:
                return res
            else:
                raise   HTTPException(status_code=404, detail="No se encontraron productos con esas cantidades")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()

#################################################    
################## CREATE ######################
async def registrar(product: productCreate):
    try:
        conn= await get_connection()
        async with conn.cursor(aio.DictCursor) as cursor:
             #TODO: hashear password = hecho en auth controller
            
            #se lanza la consulta
            await cursor.execute("INSERT INTO 202509_shop.products (title,price,quantity,status) VALUES (%s,%s,%s,%s)", (product.title, product.price, product.quantity, product.status))

            await conn.commit() #el commit no devuelve nada, solo hace el registro
            new_id = cursor.lastrowid
            new_product= await obtener_producto_by_id(new_id)
            return {"msg": "producto registrado correctamente", "item":new_product}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
    
    
    ################# HASTA AQUI OKK#########
    
    
    #TODO: ADAPTAR borrar y update   
#################################################
################## DELETE ###################### 
async def borrar_producto_by_id(product_id:int):
    product= await obtener_producto_by_id(product_id)
    if product is not None:
        try:
            conn= await get_connection()
            async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
                await cursor.execute("DELETE FROM products WHERE id=%s",(product_id,))
                await conn.commit()
            return {"msg": f'producto con id {product_id} eliminado con exito'}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
        finally:
            conn.close()
    else:
        raise HTTPException(status_code=404, detail="El producto que intentas eliminar no existe")

#################################################
################## UPDATE ######################
async def actualizar_producto_by_id(product_id: int, product: product):
    #para verificar que el producto enviado en el formulario es realmente el mismo que se busca actualizar
    if product.id != product_id:
        raise HTTPException(status_code= 400, detail= "El id no coincide")
    
    producto = await obtener_producto_by_id(product_id)
    if producto is None:
        raise HTTPException(status_code= 404, detail= "producto no encontrado")
    
    
    try:     
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("UPDATE products SET title=%s, price=%s, quantity=%s, status=%s WHERE id=%s", ( product.title, product.price, product.quantity, product.status,product.id))

            await conn.commit() #el commit no devuelve nada, solo hace el registro
            producto = await obtener_producto_by_id(product_id)
            return {"msg": "producto actualizado correctamente", "item":producto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
    

    
        