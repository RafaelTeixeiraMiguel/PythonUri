values = input()
result = []
result = values.split()

maior = int(result[0])
if(int(result[1]) > maior):
  maior = int(result[1])
if(int(result[2]) > maior):
  maior = int(result[2])
print(maior, "eh o maior")