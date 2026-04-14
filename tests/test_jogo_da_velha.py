import unittest
from src.core.jogador import Jogador
from src.core.peca import Peca
from jogos.jogo_da_velha import JogoDaVelha

class TestJogoDaVelha(unittest.TestCase):
    def setUp(self):
        self.j1 = Jogador("Alice", Peca("X"))
        self.j2 = Jogador("Bob", Peca("O"))
        self.jogo = JogoDaVelha(self.j1, self.j2)

    def test_jogada_invalida_fora_do_tabuleiro(self):
        self.assertFalse(self.jogo.aplicar_jogada(3, 3)) 

    def test_jogada_invalida_posicao_ocupada(self):
        self.jogo.aplicar_jogada(0, 0) 
        self.assertFalse(self.jogo.aplicar_jogada(0, 0)) 

    def test_vitoria_linha(self):
        self.jogo.aplicar_jogada(0, 0) 
        self.jogo.aplicar_jogada(1, 0) 
        self.jogo.aplicar_jogada(0, 1) 
        self.jogo.aplicar_jogada(1, 1) 
        self.jogo.aplicar_jogada(0, 2) 
        
        self.assertEqual(self.jogo._status, "FINALIZADO")
        self.assertEqual(self.jogo._vencedor, self.j1)

    def test_alternancia_turnos(self):
        self.assertEqual(self.jogo.jogador_atual, self.j1)
        self.jogo.aplicar_jogada(0,0)
        self.assertEqual(self.jogo.jogador_atual, self.j2)

if __name__ == "__main__":
    unittest.main()