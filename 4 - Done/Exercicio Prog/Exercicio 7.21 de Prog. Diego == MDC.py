from time import sleep


def mdc(a, b):
    valor1 = a  # Salvo os valores iniciais
    valor2 = b  # Salvo os valores iniciais

    while True:

        if a < b:  # Existe a possibilidade de b > a, logo precisa se inverter
            a, b = b, a

        if a == b:  # Crio uma condição se os números são iguais, caso aconteça, ele é divisivel por si mesmo
            divisor = a
            break

        divisor = a - b
        if divisor == b:  # Indica para a maquina se o produto da subtraçao for igual ao B, termina o processo
            break
        a = b
        b = divisor

    print()
    print("-=-" * 30)
    print("O MDC dos nº {} e o nº {} é {}".format(valor1, valor2, divisor))
    print("-=-" * 30)
    print()

    return divisor


while True:
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite um outro valor: "))

    resposta = mdc(num1, num2)

    # Nao entendi o oque o professor pediu, entao criei um "joguinho", que tu responde e a maquina executa, mais seguro
    while input("Você deseja tentar outro MDC com o valor anterior [Sim/Nao] : ").upper() == "SIM":
        num1 = resposta
        num2 = int(input("Digite um valor para fazer MDC: ").format(num1))
        resp = mdc(num1, num2)

    print()
    print("RESETANDO NOVOS VALORES....")  # Só fiz algo para deixar mais "Joguinho" / Maquina, como se tivesse processando
    sleep(2)
