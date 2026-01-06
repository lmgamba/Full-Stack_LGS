import aiomysql as aio
from db.config import *
from fastapi import HTTPException
from models.user_model import *
from core.security import *
from controllers.user_controller import obtener_usuario_by_id


async def registrar(user: UserCreate):
    try:
        conn= await get_connection()
        async with conn.cursor(aio.DictCursor) as cursor:
            #TODO: hashear password
            hashed_password= hash_password(user.password)
            
            #se lanza la consulta
            await cursor.execute("INSERT INTO 202509_shop.users (name,surname,age,mail,status,password,rol) VALUES (%s,%s,%s,%s,%s,%s,%s)", (user.name, user.surname, user.age, user.mail, user.status, hashed_password, user.rol))

            await conn.commit() #el commit no devuelve nada, solo hace el registro
            new_id = cursor.lastrowid
            new_user= await obtener_usuario_by_id(new_id)
            return {"msg": "Usuario registrado correctamente", "item":new_user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()