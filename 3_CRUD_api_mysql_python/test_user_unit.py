import pytest
from fastapi.testclient import TestClient
from main import app
import routes.user_routes as user_routes
from core.dependencies import get_current_user
from db import config

# 1. DATOS: Nuestra base de datos fake ( diccionario )
fake_users_db = {
    1: {
        "id": 1,
        "name": "Juan",
        "age": 28,
        "mail": "juan.perez@gmail.com",
        "rol": "user"
    },
    21: {
        "id": 21,
        "name": "Juan Antonio",
        "age": 43,
        "mail": "juanan@gmail.com",
        "rol": "admin"
    },
    25: {
        "id": 25,
        "name": "Pepito",
        "age": 21,
        "mail": "pepe@gmail.com",
        "rol": "user"
    }
}

#================================================
# 2. LÓGICA MOCK: Estas funciones reemplazan las llamadas a la base de datos real

async def mock_get_by_id(user_id: int):
    # Buscar el ID en nuestro diccionario en lugar de MySQL
    return fake_users_db.get(user_id)


async def mock_get_by_age(agemin: int, agemax: int):
    # Filtra el diccionario usando un for
    results = []
    for user in fake_users_db.values():
        if agemin <= user["age"] <= agemax:
            results.append(user)
    return results

# Esto es un "fusible de seguridad": hace fallar el test si intenta conectar con la BD real
async def block_real_db(*args, **kwargs):
    pytest.fail("/!\ Se intentó conectar a la base de datos REAL!")

#================================================
# 3. CONFIGURACIÓN
@pytest.fixture(autouse=True)
def setup_mocks(monkeypatch):
    # Mockeamos la conexión real a la base de datos por seguridad
    monkeypatch.setattr(config, "get_connection", block_real_db)
    
    # Reemplazamos las funciones reales del controlador dentro de las rutas por nuestros mocks
    monkeypatch.setattr(user_routes.user_controller, "obtener_usuario_by_id", mock_get_by_id)
    monkeypatch.setattr(user_routes.user_controller, "obtener_usuarios_by_age", mock_get_by_age)

@pytest.fixture
def client():
    # Proporciona el TestClient a las funciones de test
    return TestClient(app)

#================================================
# 4. AUXILIAR: Una función para simular el "login" como un usuario específico
def simulate_login(user_id: int):
    async def mock_current_user():
        return fake_users_db.get(user_id)
    
    # Le indica a FastAPI usar el mock de la funcion get
    app.dependency_overrides[get_current_user] = mock_current_user

#======================
# 5. LOS TESTS

# Test 1: El usuario puede ver sus propios datos
def test_user_can_see_own_data(client):
    # Simula ser Pepito (ID 25)
    simulate_login(25)
    # Solicita los datos de Pepito
    response = client.get("/users/25")
    assert response.status_code == 200
    assert response.json()["name"] == "Pepito"
    # Limpiamos el login para el siguiente test
    app.dependency_overrides.clear()

# Test 2: El usuario no puede ver datos de otros
def test_user_cannot_see_other_data(client):
    # Simula ser (ID 25)
    simulate_login(25)
    # Intentamos solicitar los datos de (ID 1)
    response = client.get("/users/1")
    # Debe ser 403 Forbidden por la lógica is_admin_or_owner
    assert response.status_code == 403
    app.dependency_overrides.clear()

# Test 3: El admin puede ver los datos de cualquier usuario
def test_admin_can_see_any_user(client):
    # Simula ser Admin (ID 21)
    simulate_login(21)
    # Solicita los datos de (ID 25)
    response = client.get("/users/25")
    # Al admin se le debe permitir
    assert response.status_code == 200
    assert response.json()["name"] == "Pepito"
    app.dependency_overrides.clear()

# Test 4: Filtra usuarios por edad (resultados encontrados)
def test_filter_users_by_age_range(client):
    # Filtra rango de edad 20 a 30
    params = {"agemin": 20, "agemax": 30}
    response = client.get("/users/filter/edad", params=params)
    
    assert response.status_code == 200
    data = response.json()
    # Debe encontrar a Juan (28) y Pepito (21)
    assert len(data) == 2

# Test 5: Filtra usuarios por edad (sin resultados)
def test_filter_users_by_age_returns_empty(client):
    # Filtra rango de edad 80 a 90
    params = {"agemin": 80, "agemax": 90}
    response = client.get("/users/filter/edad", params=params)
    
    assert response.status_code == 200
    # Debe devolver una lista vacía []
    assert response.json() == []