i = 0
g = 0
e = 0
qtd = 0
while(True):
  qtd+=1
  n1, n2 = input().split()
  n1 = int(n1)
  n2 = int(n2)
  if(n1 > n2):
    i += 1
  elif(n2 > n1):
    g += 1
  else:
    e += 1
  print("Novo grenal (1-sim 2-nao)")
  rsp = int(input())
  if(rsp == 2):
    break
print(qtd, "grenais")
print("Inter:{i}".format(i = i))
print("Gremio:{g}".format(g = g))
print("Empates:{e}".format(e =e))
if(n1 > n2):
  print("Inter venceu mais")
elif(n2 > n1):
  print("Gremio venceu mais")
else:
  print("Não houve vencedor")