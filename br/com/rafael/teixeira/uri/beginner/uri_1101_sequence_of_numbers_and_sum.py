n1 = 1
n2 = 1
while ((n1 > 0) & (n2 > 0)):
    soma = 0
    string = ""
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    if ((n1 > 0) & (n2 > 0)):

        if (n2 > n1):
            aux = n1
            n1 = n2
            n2 = aux
        for x in range(n2, n1 + 1):
            string += str(x) + " "
            soma += x
        string += "Sum=" + str(soma)
        print(string)