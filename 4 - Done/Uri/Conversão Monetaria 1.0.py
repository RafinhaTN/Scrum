parte_inteira = str(input(""))  # Considero Money com String
parte_decimal = str(input(""))  # Considero Centavos com String
form_dinheiro = ""
i = 0

for letra in range(len(parte_inteira) - 1, -1, -1):  # Ler de forma inversa
    form_dinheiro += parte_inteira[i]  # Adiciono letra de money na str de FORM_DINHEIRO

    if letra % 3 == 0 and letra != 0:  # Se o i for divisivel por 3, coloca a virgula na FORMATACAO_DINHEIRO
        form_dinheiro += ","

    i += 1

if len(parte_decimal) == 2:  # Fiz Gambiarra para colocar os centavos
    dinheiro_final = '{}.{}'.format(form_dinheiro, parte_decimal)
    print("${}".format(dinheiro_final))

else:
    dinheiro_final = '{}.0{}'.format(form_dinheiro, parte_decimal)
    print("${}".format(dinheiro_final))
