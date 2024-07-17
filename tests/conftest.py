import pytest

# Importa los fixtures definidos anteriormente
from backend import app, client, runner, picture

def test_health_check(client):
    # Ejemplo de prueba para la ruta /health
    res = client.get('/health')
    assert res.status_code == 200
    assert 'status' in res.json()
    assert res.json()['status'] == 'healthy'

def test_picture_endpoint(client, picture):
    # Ejemplo de prueba para una ruta que utiliza datos de 'picture'
    res = client.post('/upload_picture', json=picture)
    assert res.status_code == 200
    assert 'message' in res.json()
    assert res.json()['message'] == 'Picture uploaded successfully'
