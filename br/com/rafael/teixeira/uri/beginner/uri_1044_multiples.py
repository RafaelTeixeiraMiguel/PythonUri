values = input().split()
a = int(values[0])
b = int(values[1])

if(b > a):
  aux = a
  a = b
  b = aux

if(( a % b) == 0):
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")