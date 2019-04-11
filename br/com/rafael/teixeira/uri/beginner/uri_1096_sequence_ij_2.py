i = 1
j = 7
count = 0
for x in range (1, 16):
  print("I={i} J={j}".format(i = i, j = j))
  j -= 1
  if((x % 3 == 0) & (x != 0)):
    i += 2
    j = 7