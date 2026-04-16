# Desafio OO – Jogos de Tabuleiro

## Integrantes
- Integrante 1: Tobias Fonsatti
- Integrante 2: Guilherme Rastellii

## Arquitetura Criada
A solução foi arquitetada baseando-se nos princípios **SOLID** da Orientação a Objetos. Criamos um núcleo genérico (`src/core`) onde:
- `Peca` e `Jogador` são classes de dados base.
- `Tabuleiro` é responsável estritamente por gerenciar a matriz (encapsulamento), validar limites e armazenar o estado das peças, ignorando as regras do jogo.
- `JogoTabuleiro` é uma classe **abstrata**. Ela usa o padrão de projeto *Template Method* no método `jogar()`, delegando métodos específicos (`validar_jogada`, `aplicar_jogada`, `verificar_fim_de_jogo`) para as classes filhas (polimorfismo).

### Relações entre Objetos
- **Associação**: Um `Jogador` tem uma `Peca`.
- **Agregação**: `JogoTabuleiro` recebe uma lista de `Jogador` e um `Tabuleiro`.
- **Herança**: `JogoDaVelha` herda de `JogoTabuleiro`.

## Pontos de Extensibilidade
Para adicionar um jogo como **Lig-4**, basta criar `class Lig4(JogoTabuleiro):`, inicializar o `super().__init__` com um tabuleiro 6x7 e sobrescrever o método `aplicar_jogada` para simular a "gravidade" da peça caindo para a linha mais baixa vazia da coluna escolhida.

## Jogo(s) implementado(s)
- Jogo 1: Jogo da Velha (Tic-Tac-Toe)

## Como executar o jogo
No terminal, na raiz do projeto, digite:

'python -m src.main'

## Como executar os testes
'python -m unittest discover -s tests'

---

### Contexto acadêmico
Este projeto foi desenvolvido para um trabalho na disciplina de Programação Orientada a Objetos (POO) com Python, na FATEC em 2026.

## 📄 Licença

Este projeto é fornecido como avaliação acadêmica. Todos os direitos reservados.
