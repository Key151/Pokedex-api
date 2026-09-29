from dataclasses import dataclass
from typing import List

@dataclass
class Personagem:
    nome: str
    altura: int
    peso: int
    tipos: List[str]

    def resumo(self) -> str:
        tipos_str = " e ".join(self.tipos)
        # PokéAPI returns height in decimetres and weight in hectograms
        # To get cm and kg: height * 10, weight / 10
        return f"{self.nome.capitalize()} é do tipo {tipos_str}, pesa {self.peso / 10}kg e mede {self.altura * 10}cm"
