def fatorial(a, assistir=False):
    """
    :param a: Valor que limitará o range inverso
    :param assistir: Para mostra como foi executada a conta
    :return: Voltar o resultado optido pelo "fat"
    """
    fat = 1
    for c in range(a, 0, -1):
        if assistir:
            print(c, end=" ")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fat = fat * c

    print(fat)
    return fat


while True:
    x = int(input("Informe um valor: "))
    resp = str(input("Voce deseja visualizar sua conta:[S/N]: ")).upper()
    if resp == "S":
        m = fatorial(x, assistir=True)
    else:
        m = fatorial(x)
    print(f"{x}! =", m)