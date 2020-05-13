lista_numeros = [int(input("Digite um valor: "))]

while input("Você deseja continuar [S/N]: ").upper() != "N":
    # Enquanto a Resposta não for "N", recebe infitos valores
    valor = int(input("Digite um valor: "))
    if valor not in lista_numeros:
        # Caso esse valor não esteja na lista NUMEROS
        lista_numeros.append(valor)
    else:
        print("O valor foi DUPLICADO !!! Vou IGNORAR")

print(lista_numeros)
