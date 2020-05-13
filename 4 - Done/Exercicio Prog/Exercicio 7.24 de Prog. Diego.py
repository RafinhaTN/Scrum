from time import sleep


def quebra(n):
    """
    :param n: nº que será quebrado pela máquina
    :return: nada
    """
    primeiro_dígito = n[0]  # Leia o 1º digito
    miolo = n[1:len(n) - 1] # Leia o miolo
    ultimo_digito = n[-1]  # Leia o último digito

    print("-=-" * 30)
    print("O primeiro dígito é {}".format(primeiro_dígito))
    print("O último dígito é {}".format(ultimo_digito))
    print("O miolo do nº é {}".format(miolo))
    print("-=-" * 30)

    return False


while True:
    numero = str(input("Digite um numero: "))
    inverso = ""

    quebra(numero)  # Levo para a função a variável número

    for digito in range(len(numero) - 1, -1, -1):  # Ler o nº de forma inversa
        inverso += numero[digito]  # Inverte a ordem do nº e coloca na variavel inverso

    print("Você digitou o nº: {} \nO mesmo nº invertido é {}".format(numero, inverso))

    if numero == inverso:
        print("Temos um Palíndromo!!!")
    else:
        print("Não é um palíndromo!!!")

    print("-=-" * 30)
    sleep(0.6)
    print("RECARREGANDO PROGRAMA....")
    sleep(0.6)
    print("-=-" * 30)
