while(True):
  n1 = float(input())
  if(0 <= n1 <= 10):
    break
  else:
    print("nota invalida")

while(True):
  n2 = float(input())
  if(0 <= n2 <= 10):
    break
  else:
    print("nota invalida")
print("media = {:.2f}".format((n1 + n2)/2))