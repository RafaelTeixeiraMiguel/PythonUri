diaInicio = input()
diaInicio = diaInicio.split()
diaInicio = int(diaInicio[1])

values = input().split(" : ")
horaInicio = int(values[0])
minutoInicio = int(values[1])
segundosInicio = int(values[2])

diaTermino = input()
diaTermino = diaTermino.split()
diaTermino = int(diaTermino[1])
values = input().split(" : ")
horaTermino = int(values[0])
minutoTermino = int(values[1])
segundosTermino = int(values[2])


qtdDia = diaTermino - diaInicio
if(horaTermino < horaInicio):
  qtdDia -= 1
  qtdH = abs(horaInicio - (horaTermino + 24))
elif(horaTermino > horaInicio):
  qtdH = abs(horaInicio - horaTermino)
elif(horaTermino == horaInicio):
  qtdH = 0

if(minutoTermino < minutoInicio):
  qtdH -= 1
  qtdMin = abs(minutoInicio - (minutoTermino + 60) + 1)
elif(minutoTermino > minutoInicio):
  qtdMin = abs(minutoInicio - minutoTermino)
elif(minutoTermino == minutoInicio):
  qtdMin = 0

if(segundosTermino < segundosInicio):
  minutoTermino -= 1
  qtdSeg = abs(segundosInicio - (segundosTermino + 60))
elif(segundosTermino > segundosInicio):
  qtdSeg = abs(segundosInicio - segundosTermino)
elif(segundosTermino == segundosInicio):
  qtdSeg = 0

print(qtdDia, "dia(s)")
print(qtdH, "hora(s)")
print(qtdMin, "minuto(s)")
print(qtdSeg, "segundo(s)")