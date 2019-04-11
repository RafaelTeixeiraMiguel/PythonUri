qtd = int(input())
inInterval = 0
outInterval = 0
for x in range(0, qtd):
  n1 = int(input())
  if(10 <= n1 <= 20):
    inInterval += 1
  else:
    outInterval += 1
print("{inI} in\n{out} out".format(inI = inInterval, out = outInterval))