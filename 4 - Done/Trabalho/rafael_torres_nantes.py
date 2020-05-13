#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Rafael Torres Nantes
# Trabalho 1
# Professor(a): Diego Rubert


def bichos(n, m):
    """
    :param n: Transformo  os 2 ultimos nº de "n"
    :param m: Transformo  os 2 ultimos nº de "m"
    :return jogo_bicho: Envio um TRUE or FALSE caso aconteça ou não
    """

    n = n % 100  # Explicito que só quero os 2 ultimos nº de "n"
    m = m % 100  # Explicito que só quero os 2 ultimos nº de "m"

    if n == 00:  # O nº 100 da listinha tem 3 digitos, logo o "00" irá assumir papel de 100
        n = 100

    if m == 00:  # O nº 100 da listinha tem 3 digitos, logo o "00" irá assumir papel de 100
        m = 100

    for i in range(1, 101, 4):  # Criei uma lista que vai de 1 até 100, ao passo 4

        if i <= n < i + 4 and i <= m < i + 4:  # Identifico se "n" pertence ao mesmo grupo que "m"
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


v, n, m = input().split()  # Recebo 3 valores e corto eles
v, n, m = int(v), int(n), int(m)  # "n" = Nº Jogado e "m" = Nº sorteado

while v != 0 or n != 0 or m != 0:

    animal = bichos(n, m)  # Envio os valores para ver se eles estão no mesmo grp de animais

    if n % 10000 == m % 10000:  # Comparo se os ultimo 4 nº de "n" são iguais ao "m"
        v *= 3000

    elif n % 1000 == m % 1000:  # Comparo se os ultimo 3 nº de "n" são iguais ao "m"
        v *= 500

    elif n % 100 == m % 100:  # Comparo se os ultimo 2 nº de "n" são iguais ao "m"
        v *= 50

    elif animal == True:
        v *= 16

    else:
        v *= 0

    cedulas(v)  # Envia o valor para a função Monetária

    v, n, m = input().split()  # Recebo 3 valores e corto eles
    v, n, m = int(v), int(n), int(m)  # "n" = Nº Jogado e "m" = Nº sorteado
