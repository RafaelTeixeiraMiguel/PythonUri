n1 = int(input())
n2 = int(input())
value = 0

if(n2 > n1):
  aux = n1
  n1 = n2
  n2 = aux

for x in range(n2 + 1, n1):
  if(x % 2 != 0):
    value += x

print(value)