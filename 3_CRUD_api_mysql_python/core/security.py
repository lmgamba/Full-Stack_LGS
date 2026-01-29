import os
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from jose import jwt, JWTError

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

#crear funcion que permite codificar la contraseña usando bcrypt 
def hash_password(password: str):
    #hashear el password usando la funcion hash de bcrypt
    return pwd_context.hash(password)

#comparar el hash de mi contraseña con el de la base de datos
def verify_password(plain_password:str, hashed_password: str):    
    return pwd_context.verify(plain_password,hashed_password)


def create_token(data:dict):
    #crear token con la libreria JWT con los datos del usuario    
    data_copy_to_encode = data.copy( )
    ACCESS_TOKEN=int(ACCESS_TOKEN_EXPIRE_MINUTES)
        
        # fecha de expiracion en datetime(milisegundos)
    expire= datetime.now(tz=timezone.utc)+ timedelta(minutes=ACCESS_TOKEN)
    data_copy_to_encode.update({"expire": int(expire.timestamp())})
    
    # codificar el token
    return jwt.encode(data_copy_to_encode, SECRET_KEY,algorithm=ALGORITHM)


def decode_token(token: str):
    #decodificar el token 
    try:
        payload= jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None
    
    
    