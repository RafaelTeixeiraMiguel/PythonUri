aux = int(input())

hr = aux // 3600
aux = aux % 3600

minut = aux // 60
aux = aux % 60

print("{hora}:{min}:{seg}".format(hora = hr, min = minut, seg = aux))