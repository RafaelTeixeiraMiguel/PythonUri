while(True):
  x, y = input().split()
  x = int(x)
  y = int(y)

  if((x == 0) | (y == 0)):
    break
  elif((x > 0) & (y > 0)):
    print("primeiro")
  elif((x > 0) & (y < 0)):
    print("quarto")
  elif((x < 0) & (y > 0)):
    print("segundo")
  elif((x < 0) & (y < 0)):
    print("terceiro")