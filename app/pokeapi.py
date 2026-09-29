import requests
from models import Personagem

def montar_personagem(dados_json):
    """
    Transforma o JSON da PokéAPI em um objeto Personagem.
    """
    tipos = [t["type"]["name"] for t in dados_json["types"]]
    return Personagem(
        nome=dados_json["name"],
        altura=dados_json["height"],
        peso=dados_json["weight"],
        tipos=tipos
    )

def buscar_personagem(nome):
    """
    Busca informações de um personagem na PokéAPI.
    Retorna um objeto Personagem.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return montar_personagem(dados)
    else:
        return None
