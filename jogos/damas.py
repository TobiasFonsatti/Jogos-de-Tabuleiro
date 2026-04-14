from src.core.jogo_base import JogoTabuleiro
from src.core.tabuleiro import Tabuleiro

class DamasSimplificado(JogoTabuleiro):
    def __init__(self, jogador1, jogador2):
        
        super().__init__([jogador1, jogador2], Tabuleiro(8, 8))

    def inicializar_tabuleiro(self):
       
        for l in range(3):
            for c in range(8):
                if (l + c) % 2 != 0:
                    self._tabuleiro.posicionar_peca(l, c, self._jogadores[0].peca)
        
        
        for l in range(5, 8):
            for c in range(8):
                if (l + c) % 2 != 0:
                    self._tabuleiro.posicionar_peca(l, c, self._jogadores[1].peca)

    def validar_jogada(self, l_orig, c_orig, l_dest, c_dest) -> bool:
        t = self._tabuleiro
        
        # Regras básicas de validação
        if not (t.posicao_valida(l_orig, c_orig) and t.posicao_valida(l_dest, c_dest)):
            return False
            
        peca = t.obter_peca(l_orig, c_orig)
        if peca != self.jogador_atual.peca:
            return False 
            
        if not t.is_vazio(l_dest, c_dest):
            return False

        
        if abs(l_dest - l_orig) == 1 and abs(c_dest - c_orig) == 1:
            return True
            
      
        
        return False

    def aplicar_jogada(self, l_orig, c_orig, l_dest, c_dest) -> bool:
        if self.validar_jogada(l_orig, c_orig, l_dest, c_dest):
            # Move a peça
            peca = self._tabuleiro.remover_peca(l_orig, c_orig)
            self._tabuleiro.posicionar_peca(l_dest, c_dest, peca)
            
            
            self.alternar_turno()
            return True
        return False

    def verificar_fim_de_jogo(self) -> bool:
        
        return False 

    def jogar(self):
        """Sobrescrevemos para pedir origem e destino."""
        self.inicializar_tabuleiro()
        while self._status == "EM_ANDAMENTO":
            self._tabuleiro.exibir()
            print(f"Turno de {self.jogador_atual.nome} ({self.jogador_atual.peca})")
            
            try:
                entrada = input("Digite origem e destino (ex: 5 0 4 1): ")
                l_orig, c_orig, l_dest, c_dest = map(int, entrada.split())
                
                if not self.aplicar_jogada(l_orig, c_orig, l_dest, c_dest):
                    print("Movimento inválido! Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida! Digite 4 números (linha_origem coluna_origem linha_destino coluna_destino).")