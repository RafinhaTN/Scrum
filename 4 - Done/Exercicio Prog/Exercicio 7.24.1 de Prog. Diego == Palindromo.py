def quebra(n):
    algarismos = len(str(n))

    ultimo_digito = n % 10  # O ultimo digito

    primeiro_digito = n - (n % 10 ** (algarismos - 1))  # O primeiro digito
    primeiro_digito = n // 10 ** (algarismos - 1)

    miolo = n % 10 ** (algarismos - 1)  # É o mesmo valor que subtrai do "n" no primeiro_digito
    miolo = (miolo - ultimo_digito) // 10

    return primeiro_digito, ultimo_digito, miolo


numero = int(input("Digite um número: "))

primeiro, ultimo, miolo = quebra(numero)

print("O 1º Dígito é igual à: {}\nO último digito é igual à: {}\nO miolo é igual à: {}".format(primeiro, ultimo, miolo))

while primeiro == ultimo:
    if len(str(miolo)) == 1:
        print("-=-" * 30)
        print("O nº escrito é um PALÍNDROMO!!!")
        print("-=-" * 30)
        break
    primeiro, ultimo, miolo = quebra(miolo)

else:
    print("-=-" * 30)
    print("O nº escrito NÃO é palíndromo ('-_-)/ PUTZZ!!")
    print("-=-" * 30)
