casos = int(input())  # Quantidade de inputs que irão se prosceder
primos = []


for i in range(casos):
    num_perfect = int(input())  # Numero que será testado

    for cont in range(num_perfect - 1):  # Fiz um contador para encontrar os divisores
        cont += 1
        if num_perfect % cont == 0:  # Divisores são todos os nº que o resto é igual a 0
            primos.append(cont)   # Adiciono esse nº em uma lista
            cont += 1

    if sum(primos) == num_perfect:  # Se a soma dos nº na lista é igual ao nº descrito
        print("{} eh perfeito".format(num_perfect))

    else:
        print("{} nao eh perfeito".format(num_perfect))

    primos = []