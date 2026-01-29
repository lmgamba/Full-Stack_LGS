
from fastapi import HTTPException
from fastapi.testclient import TestClient
from fastapi import FastAPI
from main import app
import pytest


# =========================
#  SETUP: Crear versiones fake de las dependencias

# Usuario fake que se considera "logueado"
fake_current_user = {
    "id": 25,
    "name": "Pepito",
    "rol": "user"
}

fake_admin_user = {
    "id": 21,
    "name": "Juan Antonio",
    "rol": "admin"
}


# Versión fake de get_current_user que SIEMPRE devuelve el usuario logueado
async def override_get_current_user():
    return fake_current_user



# Versión fake de is_admin_or_owner 
async def override_is_admin_or_owner_as_owner(user_id: int):
    #Simula que el usuario es el dueño (id coincide)
    if fake_current_user["id"] == user_id:
        return fake_current_user
    # Si no coincide, lanza error
    raise HTTPException(status_code=403, detail="No tienes permisos")


async def override_is_admin_or_owner_as_admin(user_id: int):
    #Simula que el usuario es admin (puede acceder a todo)
    return fake_admin_user


# =========================
# FIXTURE

@pytest.fixture
def client():
    #hacer override en cada test
    yield TestClient(app)
    
    # Limpiar después
    app.dependency_overrides.clear()


# =========================
# TESTS - Usuario puede ver sus propios datos

def test_user_can_see_own_data(client):
    """
    Test: Usuario id=25 accede a /users/25 (sus datos)
    Debe: Permitirlo (200)
    """
    from main import app
    from core.dependencies import get_current_user, is_admin_or_owner
    
    # Override: hacer que el usuario actual sea id=25
    app.dependency_overrides[get_current_user] = override_get_current_user
    app.dependency_overrides[is_admin_or_owner] = override_is_admin_or_owner_as_owner
    
    # Request
    response = client.get("/users/25")
    
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.json()}")
    
    assert response.status_code == 200



# =========================
# TESTS - Usuario NO puede ver datos de otros

def test_user_cannot_see_other_data(client):
    """
    Test: Usuario id=25 intenta acceder a /users/1 (otro usuario)
    Debe: Rechazarlo (403)
    """
    from main import app
    from core.dependencies import get_current_user, is_admin_or_owner
    
    # Override: usuario actual es id=25
    app.dependency_overrides[get_current_user] = override_get_current_user
    app.dependency_overrides[is_admin_or_owner] = override_is_admin_or_owner_as_owner
    
    # Request a OTRO usuario
    response = client.get("/users/1")
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    assert response.status_code == 403
    assert "permisos" in response.json()["detail"].lower()


# =========================
#  TESTS - Admin puede ver cualquier usuario

def test_admin_can_see_any_user(client):
    """
    Test: Admin accede a /users/25 (otro usuario)
    Debe: Permitirlo (200)
    """
    from main import app
    from core.dependencies import get_current_user, is_admin_or_owner
    
    # Override: usuario actual es ADMIN
    async def override_get_admin():
        return fake_admin_user
    
    app.dependency_overrides[get_current_user] = override_get_admin
    app.dependency_overrides[is_admin_or_owner] = override_is_admin_or_owner_as_admin
    
    # Request
    response = client.get("/users/25")
    
    print(f"Status: {response.status_code}")
    
    assert response.status_code == 200



















# Base de datos fake (diccionario simple, como en docs de FastAPI)
fake_users_db = {
    1: {
        "id": 1,
        "name": "Juan",
        "surname": "Pérez García",
        "age": 28,
        "mail": "juan.perez@gmail.com",
        "status": 1,
        "rol": "user"
    },
    21: {
        "id": 21,
        "name": "Juan Antonio",
        "surname": "Pérez López",
        "age": 43,
        "mail": "juanan@gmail.com",
        "status": 1,
        "rol": "admin",
        "password": "$argon2id$v=19$m=65536,t=3,p=4$ulfq3dvb+3/vHSMkZMw55w$D+XBm7PGHGH2DSWzSdMe427iOX7YEG/aYjNEVjrEw5E"
    },
    25: {
        "id": 25,
        "name": "Pepito",
        "surname": "Pérez",
        "age": 21,
        "mail": "pepe@gmail.com",
        "status": 1,
        "rol": "user",
        "password": "$argon2id$v=19$m=65536,t=3,p=4$ulfq3dvb+3/vHSMkZMw55w$D+XBm7PGHGH2DSWzSdMe427iOX7YEG/aYjNEVjrEw5E"
    }
}





# def test_get_user_exists():
#     """
#     Test: GET /users/1 devuelve un usuario
    
#     """
#     response = client.get("/users/1")
    
#     print(f"Status: {response.status_code}")
#     print(f"Body: {response.json()}")
    
#     assert response.status_code == 200
#     assert response.json()["id"] == 1


# def test_get_user_not_found():
#     """Test: GET /users/999 (no existe)"""
#     response = client.get("/users/999")
    
#     # Puede devolver None (200) o 404, depende de tu código
#     if response.status_code == 200:
#         assert response.json() is None
#     else:
#         assert response.status_code == 404

# def test_filter_by_age():
#     """Test: GET /users/filter/edad?agemin=20&agemax=30"""
#     response = client.get("/users/filter/edad?agemin=20&agemax=30")
    
#     print(f"Users found: {len(response.json())}")
    
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)


