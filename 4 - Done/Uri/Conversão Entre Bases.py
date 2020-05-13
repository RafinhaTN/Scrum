i = 0

while True:

    number_base = input().lower().split()  # Recebo o numero e a base

    number = number_base[0]  # Decreto que o 1º item é o numero
    base = number_base[1]  # Decreto que o 1º item é o numero

    decimal = 0

    if base == "dec":  # Analiso se a base indicada é decimal

        print("Case {}:".format(i + 1))  # Escrevo o Nº do Caso
        print("{} hex".format(hex(int(number))[2:]))
        print("{} bin".format(bin(int(number))[2:]))
        print()

    if base == "bin":  # Analiso se a base indicada é binário

        for c in range(len(number)):  # Transformo o nº binário em decimal
            decimal += int(number[-1 - c]) * (2 ** c)

        print("Case {}:".format(i + 1))  # Escrevo o Nº do Caso
        print("{} dec".format(decimal))
        print("{} hex".format(hex(decimal)[2:]))
        print()


    elif base == "hex":  # Analiso se a base indicada é hexadecimal

        for c in range(len(number)):  # Transformo o nº hexadecimal em decimal

            if number[-1 - c].isnumeric():  # Caso o valor seja um númeral
                decimal += int(number[-1 - c]) * (16 ** c)

            elif number[-1 - c].isalpha():  # Caso o valor seja uma letra
                if number[-1 - c] == "a":
                    decimal += 10 * (16 ** c)
                if number[-1 - c] == "b":
                    decimal += 11 * (16 ** c)
                if number[-1 - c] == "c":
                    decimal += 12 * (16 ** c)
                if number[-1 - c] == "d":
                    decimal += 13 * (16 ** c)
                if number[-1 - c] == "e":
                    decimal += 14 * (16 ** c)
                if number[-1 - c] == "f":
                    decimal += 15 * (16 ** c)

        print("Case {}:".format(i + 1))  # Escrevo o Nº do Caso
        print("{} dec".format(decimal))
        print("{} bin".format(bin(decimal)[2:]))
        print()

    i += 1
