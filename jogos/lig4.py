from src.core.jogo_base import JogoTabuleiro
from src.core.tabuleiro import Tabuleiro

class Lig4(JogoTabuleiro):
    def __init__(self, jogador1, jogador2):
        
        super().__init__([jogador1, jogador2], Tabuleiro(6, 7))

    def inicializar_tabuleiro(self):
        # O tabuleiro começa vazio
        pass

    def validar_jogada(self, coluna: int) -> bool:
        """Valida se a coluna existe e se a linha mais alta (0) não está cheia."""
        if 0 <= coluna < self._tabuleiro.colunas:
            return self._tabuleiro.is_vazio(0, coluna)
        return False

    def aplicar_jogada(self, coluna: int) -> bool:
        if self.validar_jogada(coluna):
            
            for linha in range(self._tabuleiro.linhas - 1, -1, -1):
                if self._tabuleiro.is_vazio(linha, coluna):
                    self._tabuleiro.posicionar_peca(linha, coluna, self.jogador_atual.peca)
                    break
            
            if self.verificar_fim_de_jogo():
                self._status = "FINALIZADO"
            else:
                self.alternar_turno()
            return True
        return False

    def verificar_fim_de_jogo(self) -> bool:
        t = self._tabuleiro
        linhas, colunas = t.linhas, t.colunas
        peca_atual = self.jogador_atual.peca

        
        def checar_sequencia(l, c, dl, dc):
            for i in range(4):
                p = t.obter_peca(l + i * dl, c + i * dc)
                if p != peca_atual:
                    return False
            return True

       
        for l in range(linhas):
            for c in range(colunas):
                # Horizontal
                if c <= colunas - 4 and checar_sequencia(l, c, 0, 1):
                    self._vencedor = self.jogador_atual
                    return True
                # Vertical
                if l <= linhas - 4 and checar_sequencia(l, c, 1, 0):
                    self._vencedor = self.jogador_atual
                    return True
                # Diagonal principal (\)
                if l <= linhas - 4 and c <= colunas - 4 and checar_sequencia(l, c, 1, 1):
                    self._vencedor = self.jogador_atual
                    return True
                # Diagonal secundária (/)
                if l <= linhas - 4 and c >= 3 and checar_sequencia(l, c, 1, -1):
                    self._vencedor = self.jogador_atual
                    return True

      
        for c in range(colunas):
            if t.is_vazio(0, c):
                return False 

        self._vencedor = None
        return True 

    def jogar(self):
        """Sobrescrevemos o método jogar pois o Lig-4 pede apenas a Coluna, não linha e coluna."""
        self.inicializar_tabuleiro()
        while self._status == "EM_ANDAMENTO":
            self._tabuleiro.exibir()
            print(f"Turno de {self.jogador_atual.nome} ({self.jogador_atual.peca})")
            
            try:
                entrada = input("Digite a coluna (0 a 6): ")
                coluna = int(entrada)
                
                if not self.aplicar_jogada(coluna):
                    print("Jogada inválida! Coluna cheia ou inexistente. Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

        self._tabuleiro.exibir()
        if self._vencedor:
            print(f" O vencedor é {self._vencedor.nome}!")
        else:
            print("Empate! O tabuleiro está cheio.")