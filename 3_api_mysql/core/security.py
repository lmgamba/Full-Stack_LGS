import os
from passlib.context import CryptContext
from dotenv import load_dotenv

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