valor = int(input())
print(valor)
nota = ""
count = 0

nota = "R$ 100,00"
while(valor >= 100):
  count = count + 1
  valor -= 100
print("{qtd} nota(s) de {nota}".format(qtd = count, nota = nota))

count = 0

nota = "R$ 50,00"
while(valor >=50):
  count = count + 1
  valor -= 50
print("{qtd} nota(s) de {nota}".format(qtd = count, nota = nota))

count = 0

nota = "R$ 20,00"
while(valor >=20):
  count = count + 1
  valor -= 20
print("{qtd} nota(s) de {nota}".format(qtd = count, nota = nota))

count = 0

nota = "R$ 10,00"
while(valor >=10):
  count = count + 1
  valor -= 10
print("{qtd} nota(s) de {nota}".format(qtd = count, nota = nota))

count = 0

nota = "R$ 5,00"
while(valor >=5):
  count = count + 1
  valor -= 5
print("{qtd} nota(s) de {nota}".format(qtd = count, nota = nota))

count = 0

nota = "R$ 2,00"
while(valor >=2):
  count = count + 1
  valor -= 2
print("{qtd} nota(s) de {nota}".format(qtd = count, nota = nota))

count = 0

nota = "R$ 1,00"
while(valor >=1):
  count = count + 1
  valor -= 1
print("{qtd} nota(s) de {nota}".format(qtd = count, nota = nota))