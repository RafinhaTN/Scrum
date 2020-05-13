n = int(input("Digite um número: "))

quant_algarismos = len(str(n))  # Serve para ver quantos dígitos tem "n"

i = 1

primeiro_digito = n // 10 ** (quant_algarismos - 1)  # O "quant_dígitos" - 1 serve para extrair o 1º Dígito


while i < quant_algarismos:
    ultimo = n % 10  # Extraio o ultimo nº no resto da divisão por 10

    i += 1  # O valor de i vai aumentando até ser maior que quant_algarismos.

ultimo_digito = resto

if primeiro_digito == ultimo_digito:
    print("O nº {} tem o Primeiro e o Ultimo dígitos iguais\nSendo esse o digito: {}".format(n, primeiro_digito))

else:
    print("O nº {} não possui o Primeiro e o Ultimo dígito iguais".format(n))
    print("O Primeiro digito é : {}\nO Último dígito é : {}".format(primeiro_digito, ultimo_digito))
