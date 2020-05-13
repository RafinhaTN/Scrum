numeros = input().strip()
sequencia = numeros.split()
comprimento = 1
novo_comprimento = 1

for i in range(len(sequencia) - 1):  # Faço um i chegar na quantidade de valores na sequencia

    if int(sequencia[i]) <= int(sequencia[i + 1]):  # Caso valor anterior < posterior
        novo_comprimento += 1  # Soma-se o valor em um variavel COMPRIMENTO


    elif novo_comprimento > comprimento:
        comprimento = novo_comprimento
        novo_comprimento = 1

    else:
        novo_comprimento = 1


if novo_comprimento > comprimento:
    comprimento = novo_comprimento

print("Na sequencia: {}. O comprimento do segmento crescente máximo {}".format(numeros.replace(" ", ", "), comprimento))
