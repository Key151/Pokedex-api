from fastapi import FastAPI, HTTPException
#import sys
#import os
import requests

# Adiciona o diretório atual ao sys.path para resolver imports locais
#sys.path.append(os.path.dirname(__file__))

from pokeapi import buscar_personagem, PersonagemNaoEncontrado

app = FastAPI()

@app.get("/personagens/{nome}")
async def get_personagem(nome: str):
    try:
        personagem = buscar_personagem(nome)
        return {
            "nome": personagem.nome,
            "altura": personagem.altura,
            "peso": personagem.peso,
            "tipos": personagem.tipos,
            "resumo": personagem.resumo()
        }
    except PersonagemNaoEncontrado:
        raise HTTPException(status_code=404, detail="Personagem não encontrado na PokéAPI")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Serviço da PokéAPI temporariamente indisponível")
    except Exception as e:
        # Captura qualquer outro erro inesperado (como falhas de processamento de dados)
        raise HTTPException(status_code=500, detail=f"Erro interno ao processar personagem: {str(e)}")
