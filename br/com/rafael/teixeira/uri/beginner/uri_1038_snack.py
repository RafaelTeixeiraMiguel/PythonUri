values = input().split()

cd = int(values[0])
qtd = int(values[1])

if(cd == 1):
  print("Total: R$ {:.2f}".format(qtd * 4.00))
elif(cd == 2):
  print("Total: R$ {:.2f}".format(qtd * 4.50))
elif(cd == 3):
  print("Total: R$ {:.2f}".format(qtd * 5.00))
elif(cd == 4):
  print("Total: R$ {:.2f}".format(qtd * 2.00))
elif(cd == 5):
  print("Total: R$ {:.2f}".format(qtd * 1.50))