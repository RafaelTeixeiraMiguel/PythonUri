value = int(input())

for x in range(0,value):
  n = int(input())
  if((n > 0) & (n % 2 == 0)):
    print("EVEN POSITIVE")
  elif((n > 0) & (n % 2 != 0)):
    print("ODD POSITIVE")
  elif((n < 0) & (n % 2 == 0)):
    print("EVEN NEGATIVE")
  elif((n <0) & (n % 2 != 0)):
    print("ODD NEGATIVE")
  else:
    print("NULL")