#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Rafael Torres Nantes
# Trabalho 1
# Professor(a): Diego


def bichos(n, m):
    """
    :param n: Transformo  os 2 ultimos nº de "n"
    :param m: Transformo  os 2 ultimos nº de "m"
    :return jogo_bicho: Envio um TRUE or FALSE caso aconteça ou não
    """
    listinha = list()
    n = n[-2:: 1]  # Explicito que só quero os 2 ultimos nº de "n"
    m = m[-2:: 1]  # Explicito que só quero os 2 ultimos nº de "m"

    if n == "00":  # O nº 100 da listinha tem 3 digitos, logo o "00" irá assumir papel de 100
        n = "100"

    if m == "00":  # O nº 100 da listinha tem 3 digitos, logo o "00" irá assumir papel de 100
        m = "100"

    for i in range(0, 100, 4):  # Criei uma lista que vai de 1 até 100
        listinha = [1 + i, 2 + i, 3 + i, 4 + i]  # i soma com os valores na lista até chegar ao 100
        i += 4

        if int(n) in listinha and int(m) in listinha:
            jogo_bicho = True  # Crio uma variavel que prove se o valor é verdadeiro
            break

    else:
        jogo_bicho = False  # Se não for, ela é falsa

    return jogo_bicho


def cedulas(dinheiro):
    """
    :param dinheiro: Valor recebido depois do Jogo do Bicho
    :return nada:
    """

    c100 = dinheiro // 100
    resto = dinheiro % 100
    c10 = resto // 10
    resto = resto % 10
    c1 = resto

    print(f"{dinheiro} {c100}x100 {c10}x10 {c1}x1")

    return False


def zero(x):
    """
    ---->  Maquina criada para fazer numeros menores que 4 digitos virarem 4 digitos
    :param x: Valor que desejo fazer ficar com 4 digitos
    :return x: Retorna o valor com 4 digitos
    """
    if len(x) < 4:
        zero = int(4 - len(x))  # Vejo quantos falta para completar 4 digitos
        x = (zero * "0") + "{}".format(x)  # Multiplico os Zeros e coloco o "x"

    else:  # Nao tem o pq mudar o "x" se ele tem 4 digitos
        x = x
    return x


while True:

    v, n, m = input().split()  # Recebo 3 valores e corto eles
    v, n, m = int(v), str(n), str(m)  # "n" = Nº Jogado e "m" = Nº sorteado

    if v == 0:  # Se você não apostou, não tem pq jogar, né???
        print("Você não apostou!!!")
        exit(0)

    n = str(zero(n))  # Arrumo os valores que tem menos que 3 casas
    m = str(zero(m))  # Arrumo os valores que tem menos que 3 casas

    animal = bichos(n, m)  # Envio os valores para ver se eles estão no mesmo grp de animais

    while True:

        if n[-4:: 1] == m[-4:: 1]:  # Comparo se os ultimo 4 nº de "n" são iguais ao "m"
            v *= 3000
            break

        elif n[-3:: 1] == m[-3:: 1]:  # Comparo se os ultimo 3 nº de "n" são iguais ao "m"
            v *= 500
            break

        elif n[-2:: 1] == m[-2:: 1]:  # Comparo se os ultimo 2 nº de "n" são iguais ao "m"
            v *= 50
            break

        elif animal == True:
            v *= 16
            break

        else:
            v *= 0
            break

    cedulas(v)  # Envia o valor para a função Monetária
