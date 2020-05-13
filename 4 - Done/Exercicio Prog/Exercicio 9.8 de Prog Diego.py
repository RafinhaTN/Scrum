precis = float(input("Digite um número de precisão para o pi: "))  # O Prof. disse que seria legal colocar uma precisão
n = inverso = diferenca = 1
prim_valor = 4  # Primeiro valor da "série"
print("O valor da série é: {:.4f}".format(prim_valor))

while precis <= diferenca:  # Na realidade, não entendi direito o que ele quis com essa precisão
    n += 2   # Progressão Aritmética do Termo "n"
    inverso *= -1  # Fator que sequência soma/subtração
    post_valor = 4 / n  # Valor posterior da "série"
    pi = prim_valor + (post_valor * inverso)  # Variável que guarda a aproximação de pi

    if pi > prim_valor:  # Então... Eu não sei como ele queria essa precisão, então desculpa
        diferenca = float("{:.4f}".format(pi)) - float("{:.4f}".format(prim_valor))
    else:
        diferenca = float("{:.4f}".format(prim_valor)) - float("{:.4f}".format(pi))

    prim_valor = pi
    print("O valor da série é: {:.4f}".format(pi))
