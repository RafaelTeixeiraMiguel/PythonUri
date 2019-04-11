value = int(input())
count = 2

while(count <= value):
  print("{value}^2 = {sqr}".format(value = count, sqr = (count ** 2)))
  count += 2