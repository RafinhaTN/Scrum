valor = int(input("Digite um número: "))
numero = valor
digitos = len(str(numero))  # Descubro a quantidade de algarismos
inverso = ""  # Variavel que receberá a inversão

for algarismo in range(0, digitos):  # Leia a quantidade de digitos de forma regressiva
    inverso += str((numero % 10))  # Pego o ultimo numero e coloco em 1º na variavel INVERSO
    numero = (numero - numero % 10) // 10 # Pego os outros algarismos à esquerda

if valor == int(inverso):
    print("-=-" * 30)
    print("O nº é PALÍNDROMO!!!")
    print("-=-" * 30)

else:
    print("-=-" * 30)
    print("O nº NÃO é PALÍNDROMO!!!")
    print("-=-" * 30)
