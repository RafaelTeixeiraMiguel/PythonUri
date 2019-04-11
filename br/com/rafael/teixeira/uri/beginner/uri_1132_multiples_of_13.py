n1 = int(input())
n2 = int(input())
if(n1 > n2):
  aux = n2
  n2 = n1
  n1 = aux
soma = 0
for x in range(n1, n2+1):
  if(x % 13 != 0):
    soma +=x

print(soma)