import os
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from jose import jwt, JWTError

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

#CONFIGURAR bcrypt para usarlod entro de este fichero. Primero se activa bcrypt./!!! "argon2" es un codigo de bcrypt que podria estar deprecado, hay que revisar en la documentacion que ese codigo sea el mas actualizado o el correcto

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

#crear funcion que permite codificar la contraseña usando bcrypt => esta funcion es la que se usa dentro de auth-.controller cada vez que se registra un nuevo usuario
def hash_password(password: str):
    #hashear el password usando la funcion hash de bcrypt
    return pwd_context.hash(password)

#crear funcion para comparar el hash de mi contraseña con el de la base de datos
def verify_password(plain_password:str, hashed_password: str):
    # la funcion verify() sirve para verificar si una contraseña en texto plano coincida son su hash. 
    # ### Lo que hace es hashear de nuevo  la contraseña en texto plano  y lo compara con el hash que hay en la base de datos quitandole la "sal" a cada hash (dicha sal será diferente en cada hash)
    
    return pwd_context.verify(plain_password,hashed_password)


def create_token(data:dict):
    #crear token con la libreria JWT con los datos del usuario
    
    data_copy_to_encode = data.copy(
    )
    ACCESS_TOKEN=int(ACCESS_TOKEN_EXPIRE_MINUTES)
        #actualizar datacopy con los datos de expiracion
        
        # expire es la fecha actual + el tiempo de expiracon; es decir expire es la fecha de expiracion en datetime(milisegundos)
    expire= datetime.now(tz=timezone.utc)+ timedelta(minutes=ACCESS_TOKEN)
    data_copy_to_encode.update({"expire": int(expire.timestamp())})
    
    # codificar el token
    return jwt.encode(data_copy_to_encode, SECRET_KEY,algorithm=ALGORITHM)


def decode_token(token: str):
    #decodificar el token (payload = token decodificado)para recibir los datos del usuario (id, rol,fehca de expiracion), para lo cual se usa JWT
    try:
        #para decode es algorithmS ; no olvidar la s
        payload= jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None
    
    
    