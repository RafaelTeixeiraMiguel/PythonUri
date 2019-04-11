values = input().split()
a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])

if((b > c) & (d > a) & ((c + d) > (a + b)) & (c > 0) & (d>0) & (a % 2 == 0)):
  print("Valores aceitos")
else:
  print("Valores nao aceitos")