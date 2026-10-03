import requests
from app.models import Personagem

class PersonagemNaoEncontrado(Exception):
    """Exceção lançada quando um personagem não é encontrado na PokéAPI."""
    pass

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
    Lança PersonagemNaoEncontrado se o personagem não for encontrado (404).
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            raise PersonagemNaoEncontrado(f"Personagem '{nome}' não encontrado.")

        response.raise_for_status()

        try:
            dados = response.json()
            return montar_personagem(dados)
        except (ValueError, KeyError):
            raise Exception("Erro ao processar dados da PokéAPI")

    except requests.exceptions.Timeout:
        raise requests.exceptions.RequestException("A requisição para a PokéAPI excedeu o tempo limite.")
