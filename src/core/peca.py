class Peca:
    """Representa uma peça no tabuleiro."""
    def __init__(self, simbolo: str):
        self._simbolo = simbolo

    @property
    def simbolo(self) -> str:
        return self._simbolo

    def __str__(self):
        return self._simbolo