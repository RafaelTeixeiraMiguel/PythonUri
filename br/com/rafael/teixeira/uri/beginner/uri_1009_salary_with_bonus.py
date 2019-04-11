nome = input()
salario = float(input())
bonus = float(input())

print("TOTAL = R$ {salario:.2f}".format(salario = (salario + (bonus * 0.15))))