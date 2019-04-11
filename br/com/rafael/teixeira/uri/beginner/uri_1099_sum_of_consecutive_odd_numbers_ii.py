n = int(input())
for x in range(0, n):
  soma = 0
  n1, n2 = input().split()
  n1 = int(n1)
  n2 = int(n2)
  if(n2 > n1):
    aux = n1
    n1 = n2
    n2 = aux
  for y in range(n2 + 1, n1):
    if(y % 2 != 0):
      soma += y
  print(soma)