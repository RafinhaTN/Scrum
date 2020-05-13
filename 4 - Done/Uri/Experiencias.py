casos = int(input())  # Quantidade de inputs que irão se prosceder
r = 0  # Quantidade de Ratos
c = 0  # Quantidade de Coelhos
s = 0  # Quantidade de Sapos

for i in range(casos):
    quant_cobaia = input().lower().split()

    if quant_cobaia[1] == "r":  # Analiso se o 2º termo é igual ao anumal
        r += int(quant_cobaia[0])

    elif quant_cobaia[1] == "c":  # Analiso se o 2º termo é igual ao anumal
        c += int(quant_cobaia[0])

    elif quant_cobaia[1] == "s":  # Analiso se o 2º termo é igual ao anumal
        s += int(quant_cobaia[0])

total = r + c + s

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {:.2f} %".format((c / total) * 100))
print("Percentual de ratos: {:.2f} %".format((r / total) * 100))
print("Percentual de sapos: {:.2f} %".format((s / total) * 100))
