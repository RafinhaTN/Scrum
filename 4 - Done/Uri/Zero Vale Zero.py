while True:

    valores = input().split()
    valores = [int(x) for x in valores]

    soma = sum(valores)

    if sum(valores) > 0:
        string = str(soma)
        string = ''.join((filter(lambda x: x not in ['0'], string)))
        print(string)

    else:
        break