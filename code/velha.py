def criar_tabuleiro(dimensao):
    jogo = []
    for _ in range(dimensao):
        linha = []
        for _ in range(dimensao):
            linha.append('_')
        jogo.append(linha)
    return jogo

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        linha_str = ""
        for elemento in linha:
            linha_str += " " + elemento + " |"
        print(linha_str[:-1])
        print("-" * (4 * len(linha)))

def verificar_vitoria(tabuleiro, simbolo):
    dimensao = len(tabuleiro)
    for i in range(dimensao):
        linha_vitoria = True
        coluna_vitoria = True
        for j in range(dimensao):
            if tabuleiro[i][j] != simbolo:
                linha_vitoria = False
            if tabuleiro[j][i] != simbolo:
                coluna_vitoria = False
        if linha_vitoria or coluna_vitoria:
            return True

    diagonal1 = True
    diagonal2 = True
    for i in range(dimensao):
        if tabuleiro[i][i] != simbolo:
            diagonal1 = False
        if tabuleiro[i][dimensao-1-i] != simbolo:
            diagonal2 = False
    if diagonal1 or diagonal2:
        return True

    return False

def jogo_da_velha():
    dimensao = 3
    tabuleiro = criar_tabuleiro(dimensao)
    simbolos = ["X", "O"]
    jogador_atual = 0

    for _ in range(9):
        imprimir_tabuleiro(tabuleiro)
        linha, coluna = input(f"Jogador {jogador_atual + 1}, escolha a linha e coluna (0-{dimensao-1}) para '{simbolos[jogador_atual]}', separados por espaço: ").split()
        linha, coluna = int(linha), int(coluna)

        if tabuleiro[linha][coluna] == '_':
            tabuleiro[linha][coluna] = simbolos[jogador_atual]

            if verificar_vitoria(tabuleiro, simbolos[jogador_atual]):
                imprimir_tabuleiro(tabuleiro)
                print(f"Parabéns! O jogador {jogador_atual + 1} venceu!")
                return

            jogador_atual = 1 - jogador_atual
        else:
            print("Essa posição já está ocupada. Tente novamente.")

    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

jogo_da_velha()