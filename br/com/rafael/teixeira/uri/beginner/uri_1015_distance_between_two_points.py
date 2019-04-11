lista = []
values = input()
lista = values.split()
x1 = float(lista[0])
y1 = float(lista[1])

valores = input()
lista = valores.split()
x2 = float(lista[0])
y2 = float(lista[1])

distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

print("{:.4f}".format(distance))