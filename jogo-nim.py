def computador_escolhe_jogada(n, m):
    return min(n, m) if n <= m else n % (m + 1) or m

def usuario_escolhe_jogada(n, m):
    pecas = int(input('Quantas peças vai tirar? '))
    while not (0 < pecas <= m) or pecas > n:
        print("Oops! Jogada inválida! Tente de novo.")
        pecas = int(input("\nQuantas peças você vai tirar? "))
    return pecas

def partida():
    n = int(input('Digite o número total de peças: '))
    m = int(input('Digite o número máximo de peças por jogada: '))
    while m < 1:
        print('A quantidade de peças por jogadas devem ser menor ou igual as peças totais')
        m = int(input('Digite o número máximo de peças por jogada: '))
    pecas = 0
    jogada = 0
    if n % (m + 1) == 0:
        print('Você começa!')
        jogada = True
        while n > 0:
            jogador = "Você" if jogada == 1 else "O computador"
            pecas = usuario_escolhe_jogada(n, m) if jogada == 1 else computador_escolhe_jogada(n, m)
            print(f"{jogador} tirou {pecas}")
            n -= pecas
            print(f"Agora restam {n}")
            jogada = 2 if jogada == 1 else 1  
        vencedor = 2 if jogada == 1 else 1
        print(f"Fim do jogo! O {'computador' if vencedor == 2 else 'você'} ganhou!\n")
        return vencedor
    else:
        print("Computador começa!")
        jogada = 2 
        while n > 0:
            jogador = "O computador" if jogada == 2 else "Você"
            pecas = computador_escolhe_jogada(n, m) if jogada == 2 else usuario_escolhe_jogada(n, m)
            print(f"{jogador} tirou {pecas}")
            n -= pecas
            print(f"Agora restam {n}")
            jogada = 1 if jogada == 2 else 2
        vencedor = 2 if jogada == 1 else 1
        print(f"Fim do jogo! O {'computador' if vencedor == 2 else 'você'} ganhou!")
        return vencedor
    
def campeonato():
    quantidade_partida = 1
    placar_computador = placar_usuario = 0
    for quantidade_partida in range(1, 4):
        print("Rodada", quantidade_partida)
        if partida() == 1:
            placar_usuario += 1
        else:
            placar_computador += 1
    print("Final do campeonato!")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")
    
def main():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = solicitar_escolha()
    opcoes = {
        1: ("Você escolheu uma partida isolada!", partida),
        2: ("Você escolheu um campeonato!", campeonato)
    }
    if escolha in opcoes:
        mensagem, funcao = opcoes[escolha]
        print(mensagem)
        funcao()
    else:
        print("Opção inválida. O jogo será encerrado.")

def solicitar_escolha():
    while True:
        try:
            escolha = int(input("Escolha: "))
            if escolha in [1, 2]:
                return escolha
            else:
                print("Escolha uma opção válida!")
                continue 
        except ValueError:
            print("Por favor, insira um número válido.")
main()
