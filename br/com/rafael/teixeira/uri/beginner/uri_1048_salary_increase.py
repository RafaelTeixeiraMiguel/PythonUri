sal = float(input())

if(sal <= 400):
  a = sal * 0.15
  sal = sal + a
  r = "15 %"
elif(400 < sal <= 800):
  a = sal * 0.12
  sal = sal + a
  r = "12 %"
elif(800 < sal <= 1200):
  a = sal * 0.10
  sal = sal + a
  r = "10 %"
elif(1200 < sal <= 2000):
  a = sal * 0.07
  sal = sal + a
  r = "7 %"
elif(2000 < sal):
  a = sal * 0.04
  sal = sal + a
  r = "4 %"
print("Novo salario: {ns:.2f}\nReajuste ganho: {rg:.2f}\nEm percentual: {p}".format(ns = sal, rg = a, p = r))