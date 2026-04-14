from src.core.peca import Peca

class Tabuleiro:
    """Gerencia a grade do jogo (estado, dimensões e posicionamento)."""
    def __init__(self, linhas: int, colunas: int):
        self._linhas = linhas
        self._colunas = colunas
        self._grid = [[None for _ in range(colunas)] for _ in range(linhas)]

    @property
    def linhas(self) -> int:
        return self._linhas

    @property
    def colunas(self) -> int:
        return self._colunas

    def posicao_valida(self, linha: int, coluna: int) -> bool:
        """Verifica se a coordenada está dentro dos limites."""
        return 0 <= linha < self._linhas and 0 <= coluna < self._colunas

    def is_vazio(self, linha: int, coluna: int) -> bool:
        """Verifica se a posição está livre."""
        if not self.posicao_valida(linha, coluna):
            return False
        return self._grid[linha][coluna] is None

    def posicionar_peca(self, linha: int, coluna: int, peca: Peca) -> bool:
        """Coloca uma peça no tabuleiro se a posição for válida e vazia."""
        if self.posicao_valida(linha, coluna) and self.is_vazio(linha, coluna):
            self._grid[linha][coluna] = peca
            return True
        return False

    def obter_peca(self, linha: int, coluna: int):
        """Retorna a peça em uma dada posição, ou None."""
        if self.posicao_valida(linha, coluna):
            return self._grid[linha][coluna]
        return None

    def exibir(self):
        """Método utilitário para imprimir o tabuleiro no terminal."""
        print("\n")
        for i, linha in enumerate(self._grid):
            linha_str = " | ".join([str(peca) if peca else " " for peca in linha])
            print(f" {linha_str} ")
            if i < self._linhas - 1:
                print("-" * (self._colunas * 4 - 1))
        print("\n")

    
    def remover_peca(self, linha: int, coluna: int):
        """Remove e retorna a peça de uma posição."""
        if self.posicao_valida(linha, coluna):
            peca = self._grid[linha][coluna]
            self._grid[linha][coluna] = None
            return peca
        return None