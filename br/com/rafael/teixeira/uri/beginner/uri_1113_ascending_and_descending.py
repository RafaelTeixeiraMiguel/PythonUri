while(True):
  n1, n2 = input().split()
  n1 = int(n1)
  n2 = int(n2)
  if(n1 != n2):
    if(n1 > n2):
      print("Decrescente")
    else:
      print("Crescente")
  else:
    break