a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
h = 0
m = 0

if(c > a):
  h = a -c
elif( a > c):
  h = a - (c + 24)
elif( (a == c) & (b >= d) ):
  h = 24
elif( (a == c) & (d > b)):
  h = 0

h = abs(h)

if(d > b):
  m = b - d
elif(b > d):
  m = b - (d + 60)
  h -= 1

print("O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)".format(h = abs(h), m = abs(m)))