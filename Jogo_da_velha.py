# Jogo da velha para dois jogadores (sem ser a máquina)
import random
def printa_matriz(m):
  d = True
  for i in range(len(m)):
    for j in range(len(m[0])):
      print(f"[{m[i][j]}]", end=" ")
    print()

print("Jogador 1 (O), jogador 2 (X)\nInsira os números da linha (0, 1 ou 2) e da coluna(0, 1 ou 2) nessa ordem e separados por um espaço.")
print("................................")
quadro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
resultado = "Velha! Ninguém ganhou"
primeiro = random.randint(0, 3)
if primeiro == 1:
  print(f"Jogador 1 inicia")
  s = "X" #segundo jogador a jogar (jogador 2)
  p = "O" #primeiro jogador a jogar (jogador 1)
else:
  print("Jogador 2 inicia")
  s = "O" #segundo jogador a jogar (jogador 1)
  p = "X" #primeiro jogador a jogar (jogador 2)
for n in range(9):
  print(f"Escolha uma posição no jogo da velha:")
  printa_matriz(quadro)
  l, c = map(int, input().split(" "))
  if n % 2 == 0:
    quadro[l][c] = p
  else:
    quadro[l][c] = s
  if quadro[0][0] == quadro[0][1] == quadro[0][2] == " ":
    continue
  elif quadro[0][0] == quadro[0][1] == quadro[0][2] == "X":
    resultado = "Jogador 2 ganhou!"
    break
  elif quadro[0][0] == quadro[0][1] == quadro[0][2] == "O":
    resultado = "Jogador 1 ganhou!"
    break
  elif quadro[1][0] == quadro[1][1] == quadro[1][2] == " ":
    continue
  elif quadro[1][0] == quadro[1][1] == quadro[1][2] == "X":
    resultado = "Jogador 2 ganhou!"
    break
  elif quadro[1][0] == quadro[1][1] == quadro[1][2] == "O":
    resultado = "Jogador 1 ganhou!"
    break
  elif quadro[2][0] == quadro[2][1] == quadro[2][2] == " ":
    continue
  elif quadro[2][0] == quadro[2][1] == quadro[2][2] == "O":
    resultado = "Jogador 1 ganhou!"
    break
  elif quadro[2][0] == quadro[2][1] == quadro[2][2] == "X":
    resultado = "Jogador 2 ganhou!"
    break
  elif quadro[0][0] == quadro[1][1] == quadro[2][2] == " ":
    continue
  elif quadro[0][0] == quadro[1][1] == quadro[2][2] == "X":
    resultado = "Jogador 2 ganhou!"
    break
  elif quadro[0][0] == quadro[1][1] == quadro[2][2] == "O":
    resultado = "Jogador 1 ganhou!"
    break
  elif quadro[2][0] == quadro[1][1] == quadro[0][2] == " ":
    continue
  elif quadro[2][0] == quadro[1][1] == quadro[0][2] == "X":
    resultado = "Jogador 2 ganhou!"
    break
  elif quadro[2][0] == quadro[1][1] == quadro[0][2] == "O":
    resultado = "Jogador 1 ganhou!"
    break

print(f".................\n{resultado}")
printa_matriz(quadro)
