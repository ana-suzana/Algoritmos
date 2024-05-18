#fazer radiciação só com soma ou subtração (apenas para valores inteiros), sendo x o radicando e y o índice
x = int(input("Insira um valor para x: "))
y = int(input("Insira um valor para y: "))

if y <= 0:
  resultado = 'y inválido'

elif y == 1:
  resultado = x

elif y % 2 == 0 and x < 0:
  resultado = 'O resultado não pertence ao conjunto dos reais'

elif x == 0:
  resultado = 'raíz = 0'

elif x == 1:
  resultado = 1

else: 
  num = 2
  if x < 0:
    x = x *(-1)
    while True:
      soma = num
      for _ in range(y-1):
        base = 0
        for _ in range(num):
          base += soma
        soma = base
      if soma == x:
        resultado = num * (-1)
        break
      num += 1

  else:
    while True:
      soma = num
      for _ in range(y-1):
        base = 0
        for _ in range(num):
          base += soma
        soma = base
      if soma == x:
        resultado = num
        break
      num += 1

print(resultado)
