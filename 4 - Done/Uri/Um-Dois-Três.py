casos = int(input())
one = "one"
two = "two"

for testes in range(casos):

    numero = str(input())  # Recebo uma "Escrita de um nº"

    if len(numero) == 3:  # Caso ele tenha 3 letras, ele pode ser 1 ou 2

        numb_1 = 0
        numb_2 = 0

        for i in range(len(numero)):  # Compara letra por letra da "Escrita" e do "One"
            if one[i] == numero[i]:
                numb_1 += 1

            if two[i] == numero[i]:
                numb_2 += 1

        if numb_1 > numb_2:  # Quem tiver o maior valor dentre eles é printado
            print(1)

        elif numb_1 < numb_2:  # Quem tiver o maior valor dentre eles é printado
            print(2)

    elif len(numero) == 5:  # Se o nº tiver 5 dígitos, ele irá ser 3
        print("3")