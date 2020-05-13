def dobro(number):
    """
    :param number: Valor que será dobrado
    :return:
    """
    number *= 2


def triplo(number):
    """
    :param number: Valor que será Triplicado
    :return:
    """
    number *= 3


def fatorial(number):
    """
    :param number: Valor que será Fatorado
    :return:
    """
    fat = 1
    for cont_regre in range(number, 0, -1):
        # Contagem regressiva de "NUMBER" até "1"
        fat *= cont_regre
    print(f"O fatorial de {number} é igual à{fat}")


def fibonnaaci(number):
    """
    :param number: Posição do Fibonnaci
    :return:
    """
    # Number == Posição que eu desejo no Fibonnaci
    valor_ant, valor_post = 0, 1
    fib = 0
    cont = 2
    for cont in range(number):
        fib = valor_ant + valor_post
        valor_ant, valor_post = valor_post, fib

    print(f"O {number}º termo de Fibonnaci é {fib if number > 2 else 1}")


def primo(number):
    """
    :param number: Número que será verificado se é PRIMO
    :return:
    """
    number_primo = True
    for cont in range(2, number):
        # Começo em 2, pois exclui o "nº 0" e "1" e termina no Antecessor de NUMBER
        if number % cont == 0 :
            number_primo = False

    if number_primo:
        print("O número digitado é um Número Primo !!!")
    else:
        print("O número digitado NÃO é um Número Primo !!!")


def inverso(number):
    quant_digitos = len(str(number))
    number_invertido = ""
    for pos in range(quant_digitos):
        number_invertido += str(number % 10)
        # Obtenho o resto da Divisão de NUMBER por 10
        number = number // 10
        # Divido o Inteiro de NUMBER por 10
    print(number_invertido)