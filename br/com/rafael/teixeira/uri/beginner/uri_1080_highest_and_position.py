h = 0
index = 0
for x in range (1, 101):
  n = int(input())
  if(n > h):
    h = n
    index = x
print(h)
print(index)