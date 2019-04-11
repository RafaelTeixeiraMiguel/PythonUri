value = float(input())

print("NOTAS:")
print(int(value // 100), "nota(s) de R$ 100.00")
value = value % 100

print(int(value // 50), "nota(s) de R$ 50.00")
value = value % 50

print(int(value // 20), "nota(s) de R$ 20.00")
value = value % 20

print(int(value // 10), "nota(s) de R$ 10.00")
value = value % 10

print(int(value // 5), "nota(s) de R$ 5.00")
value = value % 5

print(int(value // 2), "nota(s) de R$ 2.00")
value = value % 2

print("MOEDAS:")
print(int(value // 1), "moeda(s) de R$ 1.00")
value = value % 1

print(int(value // 0.5), "moeda(s) de R$ 0.50")
value = value % 0.5

print(int(value // 0.25), "moeda(s) de R$ 0.25")
value = value % 0.25

print(int(value // 0.10), "moeda(s) de R$ 0.10")
value = value % 0.10

print(int(value // 0.05), "moeda(s) de R$ 0.05")
value = value % 0.05

print(int(round(value / 0.01, 0)), "moeda(s) de R$ 0.01")