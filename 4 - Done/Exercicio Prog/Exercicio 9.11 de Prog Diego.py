def inverte(n):
    invertido = ""
    for i in range(len(str(n))):  # Faço um laço para todas as bases
        invertido += "{}".format(n % 10)  # Pego o ultimo algarismo e levo para a varável
        n = (n - n % 10) // 10  # Retiro o ultimo digito
    return invertido


k = int(input("Digite o numero de teste: "))

for teste in range(k):

    number = int(input())  # Numero que será operado
    palindromo = passos = 0  # Set passos e palíndromo

    while passos < 1000:  # Número só pode ser menor que 1000 passos
        palindromo = inverte(number)  # Envia para a função inverso
        soma = int(palindromo) + number  # Faço uma variável soma

        if str(palindromo) == str(number):  # Se for palíndromo ==> Pare
            print("O número {} é palíndromo".format(number))
            print("ACABOU !!!")
            break

        print("O palíndromo do número {} é ----> {}".format(number, palindromo))
        print("A soma do Palídromo e o Original é igual a: {}".format(soma))

        number = soma
        passos += 1
    else:
        print("??")
