from fastapi import FastAPI, HTTPException
import sys
import os

# Adiciona o diretório atual ao sys.path para resolver imports locais
sys.path.append(os.path.dirname(__file__))

from pokeapi import buscar_personagem

app = FastAPI()

@app.get("/personagens/{nome}")
async def get_personagem(nome: str):
    personagem = buscar_personagem(nome)
    if personagem:
        return {
            "nome": personagem.nome,
            "altura": personagem.altura,
            "peso": personagem.peso,
            "tipos": personagem.tipos,
            "resumo": personagem.resumo()
        }
    raise HTTPException(status_code=404, detail="Personagem não encontrado")
