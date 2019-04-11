values = input().split()


a = float(values[0])
b = float(values[1])
c = float(values[2])

if(c > b):
  aux = b
  b = c
  c = aux
if(b > a):
  aux = a
  a = b
  b = aux
if(c > b):
  aux = b
  b = c
  c = aux

if((a >= (b + c))):
  print("NAO FORMA TRIANGULO")
else:
  if(((a ** 2) == ((b ** 2)+ (c ** 2)))):
    print("TRIANGULO RETANGULO")

  if( (a ** 2) > ((b ** 2) + (c ** 2)) ):
    print("TRIANGULO OBTUSANGULO")

  if(((a ** 2) < ((b ** 2) + (c ** 2)))):
    print("TRIANGULO ACUTANGULO")

  if(a == b == c):
    print("TRIANGULO EQUILATERO")

  if((a == b != c) | (a == c != b) | (c == b != a)):
    print("TRIANGULO ISOSCELES")