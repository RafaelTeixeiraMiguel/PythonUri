values = input().split()
n1 = float(values[0])
n2 = float(values[1])
n3 = float(values[2])
n4 = float(values[3])

m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print("Media: {:.1f}".format(m))

if(m < 5.0):
  print("Aluno reprovado.")
elif(m >= 7.0):
  print("Aluno aprovado.")
else:
  print("Aluno em exame.")
  ex = float(input())
  print("Nota do exame: {:.1f}".format(ex))
  m = (m + ex) / 2
  if(m >= 5):
    print("Aluno aprovado.")
  else:
    print("Aluno reprovado.")
  print("Media final: {:.1f}".format(m))