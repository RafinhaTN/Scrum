# -*- coding: utf-8 -*-

while True:
    inteiro = int(input(""))
    decimal = float(input(""))

    dinheiro = "{:.2f}".format(inteiro + (decimal/100)) #Criei uma String que junta a parte inteira e a decimal

    number = dinheiro.split(".") #Dps eu cortei ela
    money = number[0]

    form_dinheiro = ""
    i = 0

    for letra in range(len(money) - 1, -1, -1): #Ler de forma inversa
        form_dinheiro += money[i] #Adiciono letra de money na str de FORM_DINHEIRO

        if letra % 3 == 0 and letra != 0: #Se o i for divisivel por 3, coloca a virgula na FORMATACAO_DINHEIRO
            form_dinheiro += ","

        i += 1

    print("${}.{}".format(form_dinheiro, number[1]))