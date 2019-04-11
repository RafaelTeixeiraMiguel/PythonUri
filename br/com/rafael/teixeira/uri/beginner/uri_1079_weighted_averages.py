qtd = int(input())
for x in range (0, qtd):
  n1, n2, n3 = input().split()
  n1 = float(n1)
  n2 = float(n2)
  n3 = float(n3)

  print("{:.1f}".format(((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)))