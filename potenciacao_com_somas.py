#Fazer x**y só usando soma ou subtração
x = int(input("Insira um valor para x: "))
y = int(input("Insira um valor para y: "))
soma = x

if y > 1:
  if x < 0:
    x = x * (-1)
    for _ in range(y-1):
      base = 0
      for _ in range(x):
        base += soma
      soma = base
    if y % 2 == 0:
      base = base * (-1)

  else:
    for _ in range(y-1):
      base = 0
      for _ in range(x):
        base += soma
      soma = base

elif y == 0:
  if x == 0:
    base = '0 ** 0 = Indefinido'
  else:
    base = 1

elif y == 1:
  base = x

else:
  base = 'Valores inválidos'

print(base)
