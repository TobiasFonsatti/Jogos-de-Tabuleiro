from src.core.jogo_base import JogoTabuleiro
from src.core.tabuleiro import Tabuleiro

class JogoDaVelha(JogoTabuleiro):
    def __init__(self, jogador1, jogador2):
        
        super().__init__([jogador1, jogador2], Tabuleiro(3, 3))

    def inicializar_tabuleiro(self):
        # No jogo da velha, o tabuleiro começa vazio.
        pass

    def validar_jogada(self, linha: int, coluna: int) -> bool:
        return self._tabuleiro.is_vazio(linha, coluna)

    def aplicar_jogada(self, linha: int, coluna: int) -> bool:
        if self.validar_jogada(linha, coluna):
            peca = self.jogador_atual.peca
            self._tabuleiro.posicionar_peca(linha, coluna, peca)
            
            if self.verificar_fim_de_jogo():
                self._status = "FINALIZADO"
            else:
                self.alternar_turno()
            return True
        return False

    def verificar_fim_de_jogo(self) -> bool:
        t = self._tabuleiro
        
        
        for i in range(3):
            # Linhas
            if t.obter_peca(i, 0) and t.obter_peca(i, 0) == t.obter_peca(i, 1) == t.obter_peca(i, 2):
                self._vencedor = self.jogador_atual
                return True
            # Colunas
            if t.obter_peca(0, i) and t.obter_peca(0, i) == t.obter_peca(1, i) == t.obter_peca(2, i):
                self._vencedor = self.jogador_atual
                return True

        
        if t.obter_peca(0, 0) and t.obter_peca(0, 0) == t.obter_peca(1, 1) == t.obter_peca(2, 2):
            self._vencedor = self.jogador_atual
            return True
        if t.obter_peca(0, 2) and t.obter_peca(0, 2) == t.obter_peca(1, 1) == t.obter_peca(2, 0):
            self._vencedor = self.jogador_atual
            return True

       
        vazio = False
        for l in range(3):
            for c in range(3):
                if t.is_vazio(l, c):
                    vazio = True
        
        if not vazio:
            self._vencedor = None
            return True 

        return False 