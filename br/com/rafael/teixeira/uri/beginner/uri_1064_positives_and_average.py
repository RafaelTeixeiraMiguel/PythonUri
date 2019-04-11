count = 0
media = 0
n1 = float(input())
if(n1 > 0):
  count += 1
  media += n1
n2 = float(input())
if(n2 > 0):
  count += 1
  media += n2
n3 = float(input())
if(n3 > 0):
  count += 1
  media += n3
n4 = float(input())
if(n4 > 0):
  count += 1
  media += n4
n5 = float(input())
if(n5 > 0):
  count += 1
  media += n5
n6 = float(input())
if(n6 > 0):
  count += 1
  media += n6
media = media / count
print("{n} valores positivos".format(n = count))
print("{:.1f}".format(media))