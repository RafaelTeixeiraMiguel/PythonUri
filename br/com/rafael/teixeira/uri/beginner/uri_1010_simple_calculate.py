x = 0
total = 0
for x in range(0,2):
    values = input()
    array = []
    array = values.split()
    cd = int(array[0])
    qtd = int(array[1])
    price = float(array[2])
    total += qtd * price
print("VALOR A PAGAR: R$ {total:.2f}".format(total = total))