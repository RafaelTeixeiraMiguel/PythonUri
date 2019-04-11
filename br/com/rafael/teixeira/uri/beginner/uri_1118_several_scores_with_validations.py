rsp = 1
while (rsp == 1):
    while (True):
        n1 = float(input())
        if (0 <= n1 <= 10):
            break
        else:
            print("nota invalida")

    while (True):
        n2 = float(input())
        if (0 <= n2 <= 10):
            break
        else:
            print("nota invalida")
    print("media = {:.2f}".format((n1 + n2) / 2))

    while (True):
        print("novo calculo (1-sim 2-nao)")
        rsp = int(input())
        if ((rsp == 1) | (rsp == 2)):
            break