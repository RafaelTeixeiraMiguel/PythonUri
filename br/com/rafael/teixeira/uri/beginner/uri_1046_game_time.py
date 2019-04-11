a, b = input().split()
a = int(a)
b = int(b)

if(b > a):
  print("O JOGO DUROU {h} HORA(S)".format(h = abs(a - b)))
elif(a > b):
  print("O JOGO DUROU {h} HORA(S)".format(h = abs(a - (b + 24))))
else:
  print("O JOGO DUROU 24 HORA(S)")