decimal = int(input("Digite um nº inteiro: "))

print("""Escolha a base que deseja converter:
[1]BINARIO
[2]OCTAL
[3]HEXADECIMAL""")

base = int(input("Sua opção é: "))


if base == 1:
    print(f"O valor {decimal} em binário é {bin(decimal)[2:]}")
elif base == 2:
    print(f"O valor {decimal} em octal é {oct(decimal)[2:]}")
elif base == 3:
    print(f"O valor {decimal} em hexadecimal é {hex(decimal)[2:]}")