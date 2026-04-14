from src.core.peca import Peca

class Jogador:
    """Representa um jogador e sua respectiva peça."""
    def __init__(self, nome: str, peca: Peca):
        self._nome = nome
        self._peca = peca

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def peca(self) -> Peca:
        return self._peca
        
    def __str__(self):
        return self._nome