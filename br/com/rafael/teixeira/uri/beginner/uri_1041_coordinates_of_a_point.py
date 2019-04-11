values = input().split()

x = float(values[0])
y = float(values[1])

if(0.0 == x == y):
  print("Origem")
elif((x > 0.0) & (y > 0.0)):
  print("Q1")
elif((x > 0.0) & (y < 0.0)):
  print("Q4")
elif((x < 0.0) & (y > 0.0)):
  print("Q2")
elif((x < 0.0) & (y < 0.0)):
  print("Q3")
elif(x == 0.0):
  print("Eixo Y")
elif(y == 0.0):
  print("Eixo X")