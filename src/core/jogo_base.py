from abc import ABC, abstractmethod
from typing import List
from src.core.jogador import Jogador
from src.core.tabuleiro import Tabuleiro

class JogoTabuleiro(ABC):
    """Classe base abstrata para qualquer jogo de tabuleiro."""
    def __init__(self, jogadores: List[Jogador], tabuleiro: Tabuleiro):
        self._jogadores = jogadores
        self._tabuleiro = tabuleiro
        self._turno_atual = 0
        self._status = "EM_ANDAMENTO"
        self._vencedor = None

    @property
    def jogador_atual(self) -> Jogador:
        return self._jogadores[self._turno_atual % len(self._jogadores)]

    def alternar_turno(self):
        self._turno_atual += 1

    @abstractmethod
    def inicializar_tabuleiro(self):
        """Prepara o estado inicial do tabuleiro (ex: colocar peças de xadrez)."""
        pass

    @abstractmethod
    def validar_jogada(self, *args) -> bool:
        """Regras específicas do jogo para validar uma jogada."""
        pass

    @abstractmethod
    def aplicar_jogada(self, *args) -> bool:
        """Executa a jogada e atualiza o estado do jogo."""
        pass

    @abstractmethod
    def verificar_fim_de_jogo(self) -> bool:
        """Verifica se há vitória, derrota ou empate."""
        pass
        
    def jogar(self):
        """Loop principal do jogo (Pode ser sobrescrito para interfaces gráficas)."""
        self.inicializar_tabuleiro()
        while self._status == "EM_ANDAMENTO":
            self._tabuleiro.exibir()
            print(f"Turno de {self.jogador_atual.nome} ({self.jogador_atual.peca})")
            
           
            try:
                entrada = input("Digite a linha e coluna separados por espaço (ex: 0 2): ")
                linha, coluna = map(int, entrada.split())
                
                if not self.aplicar_jogada(linha, coluna):
                    print("Jogada inválida! Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida! Digite números válidos.")

        self._tabuleiro.exibir()
        if self._vencedor:
            print(f" O vencedor é {self._vencedor.nome}! ")
        else:
            print("Empate! Deu velha.")