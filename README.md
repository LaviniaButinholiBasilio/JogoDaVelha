# 🖥️ Jogo da Velha (Python - Terminal)

![Feito com Python](https://img.shields.io/badge/feito%20com-Python-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-success)
![Licença](https://img.shields.io/badge/licença-Livre-blue)
![Autoria](https://img.shields.io/badge/feito%20por-Lavínia%20Butinholi%20Basílio-lightgrey)

---

## 📖 Descrição
Este projeto implementa o clássico **Jogo da Velha** (*Tic-Tac-Toe*) em **Python**, totalmente jogável no **terminal**.  
O foco é a **lógica do jogo** — criação do tabuleiro, alternância entre jogadores, verificação de vitória e detecção de empate.

---

## ⚙️ Funcionalidades
- 🧩 Criação dinâmica do tabuleiro (por padrão 3x3)  
- 🔄 Alternância automática entre os jogadores **X** e **O**  
- ✅ Verificação de vitória em linhas, colunas e diagonais  
- 🤝 Detecção de empate  
- 💬 Interface simples via terminal  

---

## 🧠 Estrutura do Código
| Função | Descrição |
|--------|------------|
| `criar_tabuleiro(dimensao)` | Cria uma matriz NxN com espaços vazios (`_`) |
| `imprimir_tabuleiro(tabuleiro)` | Exibe o tabuleiro formatado no terminal |
| `verificar_vitoria(tabuleiro, simbolo)` | Verifica se o jogador venceu |
| `jogo_da_velha()` | Controla o fluxo principal do jogo |

---

## 🚀 Como Executar

### 1️⃣ Pré-requisitos
- Ter o **Python 3** instalado no sistema

### 2️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/jogo-da-velha.git
cd jogo-da-velha
python jogo_da_velha.py

## 🎮 Como Jogar

1. O terminal exibirá o tabuleiro com posições vazias (`_`).  
2. Cada jogador, por vez, escolhe uma **linha** e uma **coluna** digitando dois números separados por espaço (ex: `0 2`).  
3. O símbolo (**X** ou **O**) será marcado na posição escolhida.  
4. O jogo continua até que um jogador vença ou todas as posições sejam preenchidas (empate).

**Exemplo de rodada:**

 _ | _ | _
------------
 _ | _ | _
------------
 _ | _ | _

Jogador 1, escolha a linha e coluna (0-2) para 'X', separados por espaço: 1 1


## 👩‍💻 Autor

**Lavínia Butinholi Basílio**  
Projeto criado para fins de estudo em **lógica de programação**, **estruturas de repetição** e **funções em Python**.


## 🪶 Licença

Este projeto é de **uso livre** para fins **educacionais e de aprendizado**.  
Sinta-se à vontade para estudar, modificar e aprimorar. 💡
