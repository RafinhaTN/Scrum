def Fib(n):
    """
    :param n: Termo do Fibonacci
    :return:
    """
    f1 = 1
    f2 = 1

    i = 2  # Nº de termos que a máquina já passou

    while i < n:
        soma = f1 + f2

        f1 = f2  # O 2º termo virará o 1º
        f2 = soma  # E o resultado da soma irá tornar-se o 2º
        i += 1

    return soma


termo = int(input("Digite um termo: "))

if termo >= 3:  # Se o nº de termos for maior que 2, ele leva para a função Fib
    resp = Fib(termo)

else:  # Caso contrário o valor será "1", pois o 1º e o 2º termo são iguais a 1
    resp = 1

print("O {}º termo na sequência de Fibonacci é {}".format(termo, resp))
