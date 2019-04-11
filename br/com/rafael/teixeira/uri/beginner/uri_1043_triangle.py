values = input().split()
a = float(values[0])
b = float(values[1])
c = float(values[2])

if(((a + b) > c) & ((a + c) > b) & ((b + c) > a)):
  print("Perimetro = {:.1f}".format((a + b + c)))
else:
  print("Area = {:.1f}".format(((a + b) * c) / 2))