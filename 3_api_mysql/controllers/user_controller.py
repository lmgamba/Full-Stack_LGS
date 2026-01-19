from db.config import *
from fastapi import HTTPException , Depends, Path
from models.user_model import *
import aiomysql as aio

#AQUI SE CONECTA A LA DATABASE

async def obtener_usuario_by_id(user_id):
    try:
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("SELECT * FROM users WHERE id=%s",(user_id,))
            user=await cursor.fetchone()
            return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
        
        
#obtener usuarios entre un rango de edades

async def obtener_usuarios_by_age(agemin,agemax):
    
    if agemin > agemax:
        raise   HTTPException(status_code=400, detail="La edad min no puede ser mayor a la maxima")
    
    try:
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("SELECT * FROM users WHERE users.age BETWEEN %s AND %s ",(agemin,agemax))
            res=await cursor.fetchall()
            if len(res) != 0:
                return res
            else:
                raise   HTTPException(status_code=404, detail="No se encontraron usuarios entre esas edades")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
        
async def registrar(user: UserCreate):
    try:
        conn= await get_connection()
        async with conn.cursor(aio.DictCursor) as cursor:
            #TODO: hashear password = hecho en auth controller
            
            #se lanza la consulta
            await cursor.execute("INSERT INTO 202509_shop.users (name,surname,age,mail,status,password,rol) VALUES (%s,%s,%s,%s,%s,%s,%s)", (user.name, user.surname, user.age, user.mail, user.status, user.password, user.rol))

            await conn.commit() #el commit no devuelve nada, solo hace el registro
            new_id = cursor.lastrowid
            new_user= await obtener_usuario_by_id(new_id)
            return {"msg": "Usuario registrado correctamente", "item":new_user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
        
async def borrar_usuario_by_id(user_id:int):
    user= await obtener_usuario_by_id(user_id)
    if user is not None:
        try:
            conn= await get_connection()
            async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
                await cursor.execute("DELETE FROM users WHERE id=%s",(user_id,))
                await conn.commit()
            return {"msg": f'Usuario con id {user_id} eliminado con exito'}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
        finally:
            conn.close()
    else:
        raise HTTPException(status_code=404, detail="El ususario que intentas eliminar no existe")



async def actualizar_usuario_by_id(user_id, user: User):
    #para verificar que el usuario enviado en el formulario es realmente el mismo que se busca actualizar
    if user.id != user_id:
        raise HTTPException(status_code= 400, detail= "El id no coincide")
    
    usuario = await obtener_usuario_by_id(user_id)
    if usuario is None:
        raise HTTPException(status_code= 404, detail= "Usuario no encontrado")
    
    
    try:     
        conn= await get_connection()
        #abrir sql para lanzar queries
        async with conn.cursor(aio.DictCursor) as cursor:
            #se lanza la consulta
            await cursor.execute("UPDATE users SET name=%s, surname=%s, age=%s, mail=%s, status=%s, password=%s, rol=%s WHERE id=%s", ( user.name, user.surname, user.age, user.mail, user.status, user.password, user.rol,user.id))

            await conn.commit() #el commit no devuelve nada, solo hace el registro
            usuario = await obtener_usuario_by_id(user_id)
            return {"msg": "Usuario actualizado correctamente", "item":usuario}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
    