qtd = int(input())
for x in range(0, qtd):
  x, y = input().split()
  x = int(x)
  y = int(y)
  if(y == 0):
    print("divisao impossivel")
  else:
    print(x / y)