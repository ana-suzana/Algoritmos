def cria_matriz(linhas, colunas):
  return [[random.randint(-9, 9) for _ in range(linhas)] for _ in range(colunas)]

def determinante(matriz):
  det = 0
  for i in range(3):
    det += matriz[0][i] * matriz[1][i+1] * matriz[2][i+2]
  for i in range(4, 1, -1):
    det -= matriz[0][i] * matriz[1][i-1] * matriz[2][i-2]
  return det

def imprimir_matriz(matriz):
  for l in range(len(matriz)):
    for c in range(len(matriz[0])):
      print(f"[{matriz[l][c]:^5}]", end="")
    print()
  print()

print("DETERMINANTE DE MATRIZES 3x3")
r = int(input("Digite 1 para inserir uma matriz ou 2 para gerá-la aleatoriamente: "))
if r == 2:
  m = cria_matriz(3, 3)
else:
  m = []
  for i in range(4):
    lista = []
    for j in range(3):
      num = int(input())
      lista.append(num)
    m.append(lista)

imprimir_matriz(m)

for k in range(3):
  m[k].extend(m[k][0:2])

print("Determinante =", determinante(m))
