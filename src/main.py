from src.core.jogador import Jogador
from src.core.peca import Peca
from jogos.jogo_da_velha import JogoDaVelha
from jogos.lig4 import Lig4
from jogos.damas import DamasSimplificado

def main():
    print("=== Bem-vindo aos Jogos de Tabuleiro ===")
    
    nome1 = input("Nome do Jogador 1: ") or "Jogador 1"
    nome2 = input("Nome do Jogador 2: ") or "Jogador 2"
    
    print("\nEscolha o jogo:")
    print("1 - Jogo da Velha")
    print("2 - Lig-4")
    print("3 - Damas (Simplificado)")
    
    escolha = input("Digite o número do jogo: ")
    
    if escolha == "1":
        jogador1 = Jogador(nome1, Peca("X"))
        jogador2 = Jogador(nome2, Peca("O"))
        jogo = JogoDaVelha(jogador1, jogador2)
        
    elif escolha == "2":
        # Lig4 geralmente usa cores ou símbolos cheios
        jogador1 = Jogador(nome1, Peca("🔴")) 
        jogador2 = Jogador(nome2, Peca("🟡"))
        jogo = Lig4(jogador1, jogador2)
        
    elif escolha == "3":
        jogador1 = Jogador(nome1, Peca("B"))
        jogador2 = Jogador(nome2, Peca("P"))
        jogo = DamasSimplificado(jogador1, jogador2)
        
    else:
        print("Opção inválida. Encerrando.")
        return

    # O polimorfismo brilha aqui: não importa qual jogo foi instanciado, 
    # o método jogar() sabe exatamente o que fazer!
    jogo.jogar()

if __name__ == "__main__":
    main()