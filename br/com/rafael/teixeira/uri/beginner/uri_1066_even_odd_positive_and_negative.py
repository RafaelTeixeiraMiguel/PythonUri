par = 0
impar = 0
negativo = 0
positivo = 0

n1 = float(input())
if(n1 % 2 == 0):
  par += 1
else:
  impar += 1
if(n1 > 0):
  positivo += 1
elif(n1 < 0):
  negativo += 1

n1 = float(input())
if(n1 % 2 == 0):
  par += 1
else:
  impar += 1
if(n1 > 0):
  positivo += 1
elif(n1 < 0):
  negativo += 1

n1 = float(input())
if(n1 % 2 == 0):
  par += 1
else:
  impar += 1
if(n1 > 0):
  positivo += 1
elif(n1 < 0):
  negativo += 1

n1 = float(input())
if(n1 % 2 == 0):
  par += 1
else:
  impar += 1
if(n1 > 0):
  positivo += 1
elif(n1 < 0):
  negativo += 1

n1 = float(input())
if(n1 % 2 == 0):
  par += 1
else:
  impar += 1
if(n1 > 0):
  positivo += 1
elif(n1 < 0):
  negativo += 1

print("{n} valor(es) par(es)".format(n = par))
print("{n} valor(es) impar(es)".format(n = impar))
print("{n} valor(es) positivo(s)".format(n = positivo))
print("{n} valor(es) negativo(s)".format(n = negativo))