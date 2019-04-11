qtd = int(input())
total = 0
qtdCoelho = 0
qtdRato = 0
qtdSapo = 0
for x in range(0, qtd):
  amount, tipo = input().split()
  amount = int(amount)
  total += amount
  if(tipo.lower() == "c"):
    qtdCoelho += amount
  elif(tipo.lower() == "r"):
    qtdRato += amount
  elif(tipo.lower() == "s"):
    qtdSapo += amount
print("Total: {total} cobaias".format(total = total))
print("Total de coelhos: {coelho}".format(coelho = qtdCoelho))
print("Total de ratos: {rato}".format(rato = qtdRato))
print("Total de sapos: {sapo}".format(sapo = qtdSapo))
print("Percentual de coelhos: {percentualCoelho:.2f} %".format(percentualCoelho = (qtdCoelho * 100) / total))
print("Percentual de ratos: {percentualRato:.2f} %".format(percentualRato = (qtdRato * 100) / total))
print("Percentual de sapos: {percentualSapo:.2f} %".format(percentualSapo = (qtdSapo * 100) / total))