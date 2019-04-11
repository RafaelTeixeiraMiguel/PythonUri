values = input().split()

a = float(values[0])
b = float(values[1])
c = float(values[2])

delta = (((b ** 2) -4 * (a * c)))
if(delta > 0):
  delta = delta ** (1/2)
else:
  delta = -1
divided = 2 * a

if((delta >= 0) & (divided != 0)):
  x2 = (-b - delta) / divided
  x1 = (-b + delta) / divided
  print("R1 = {x1:.5f}\nR2 = {x2:.5f}".format(x1 = x1, x2 = x2))
else:
  print("Impossivel calcular")