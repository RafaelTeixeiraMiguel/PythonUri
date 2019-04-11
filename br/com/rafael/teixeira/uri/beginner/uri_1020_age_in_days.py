days = int(input())

ano = days // 365
days = days % 365
mes = days // 30
days = days % 30
days = "{:.0f}".format(days)

print("{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)".format(anos = ano, meses = mes, dias = days))