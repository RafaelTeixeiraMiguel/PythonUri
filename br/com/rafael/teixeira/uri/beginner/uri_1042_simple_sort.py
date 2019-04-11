values = input().split()

a = int(values[0])
b = int(values[1])
c = int(values[2])
aux = 0
if(b > a):
  aux = a
  a = b
  b = aux
if(c > b):
  aux = b
  b = c
  c = aux
if(b > a):
  aux = a
  a = b
  b = aux
print(c)
print(b)
print(a)
print()
print(values[0])
print(values[1])
print(values[2])