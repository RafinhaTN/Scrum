from time import sleep


def mdc(a, b):
    """
    ---> Maquina para fazer MDC usando Euclides (apesar de existir um método mais eficiente e simples)
    :param a: valor que será o dividendo da equação
    :param b: valor que será o divisor da equação
    :return retornado: valor que retorna para executar outros teste
    """

    valor1 = a  # Salvo o valores A inicial em outra variável para aplicar no print (Estética)
    valor2 = b  # Salvo o valores B inicial outra variável para aplicar no print (Estética)

    while True:

        if a < b:  # Existe a possibilidade de b > a, logo precisa se inverter
            a, b = b, a

        divisor = a % b

        if a == b:  # Crio uma condição se os números são iguais, caso aconteça, ele é divisivel por si mesmo
            divisor = a
            break

        if divisor == 0:  # Indica para a maquina resto da divisão for igual a 0, divisor max é o próprio b
            divisor = b
            break
        a = b  # Os valores vão se alternando para chegar em um resto = 0
        b = divisor

    print()
    print("-=-" * 30)
    print("O MDC do nº {} e nº {} ===== \033[33m{}\033[m ".format(valor1, valor2, divisor))
    print("-=-" * 30)
    print()
    return divisor


n = int(input("A quantidade de nº que deseja fazer o MDC: "))

print()
print("INICIANDO......")
print()
sleep(0.5)

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um outro valor: "))

i = 2

resp = mdc(num1, num2)

while i < n:  # Cicla os demais valores não lidos, e decreta o nº de vezes restante
    num1 = resp
    num2 = int(input("Digite um outro valor para fazer MDC: "))
    resp = mdc(num1, num2)
    i += 1
