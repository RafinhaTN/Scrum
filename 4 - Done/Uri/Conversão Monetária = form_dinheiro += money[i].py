while True:
    parte_initeira = int(input(""))
    parte_decimal = float(input(""))

    dinheiro = "{:.2f}".format(parte_initeira + (parte_decimal / 100))
    # Criei uma String que junta a parte inteira e a decimal

    dinheiro = dinheiro.split(".")
    # Cortei a variável DINHEIRO(parte_initeira + parte_decimal)

    parte_initeira = dinheiro[0]
    # Determino a Parte Inteira

    form_dinheiro = ""
    i = 0

    for pos in range(len(parte_initeira) - 1, -1, -1):  # Ler de forma inversa
        form_dinheiro += parte_initeira[i]
        # Adiciono POS de money na str de FORM_DINHEIRO

        if pos % 3 == 0 and pos != 0:
            # Se a Posição for Divisivel por 3, coloca a virgula na FORMATACAO_DINHEIRO
            form_dinheiro += ","

        i += 1

    print("${}.{}".format(form_dinheiro, dinheiro[1]))
    # Printo a Parte Inteira Formatada "." Parte Decimal
