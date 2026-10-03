# Pokédex API

Uma API REST construída com Python e FastAPI que consome dados de personagens de jogos retrô (Pokémon) via [PokéAPI](https://pokeapi.co/).

Projeto desenvolvido durante a trilha 7 Days of Code — Vibe Coding com Claude Code, da Alura.

## Objetivo
Este projeto é parte da trilha 7 Days of Code — Vibe Coding com Claude Code, onde construímos uma API do zero guiando um agente de IA como parceiro de programação.

## Como rodar
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Rodar a aplicação
uvicorn app.main:app --reload
```
## Tecnologias
- Python 3.11+
- FastAPI — Framework web assíncrono
- Uvicorn — Servidor ASGI
- Requests — Consumo de APIs externas
- Pytest — Testes automatizados
