import sys
import os

# Primeiro ajusta o path...
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ...depois importa
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_pikachu_success():
    """
    Verifica se o endpoint /personagens/pikachu retorna 200 e o nome correto.
    """
    response = client.get("/personagens/pikachu")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "pikachu"

def test_get_nonexistent_pokemon_404():
    """
    Verifica se o endpoint /personagens/personagem-inexistente retorna 404.
    """
    response = client.get("/personagens/personagem-inexistente")
    assert response.status_code == 404
    data = response.json()
    assert "Personagem não encontrado na PokéAPI" in data["detail"]