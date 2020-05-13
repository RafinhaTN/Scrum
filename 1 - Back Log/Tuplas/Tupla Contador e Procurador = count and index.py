numeros = (int(input("Digite um número: ")),
           int(input("Digite outro número: ")),
           int(input("Digite mias um número: ")),
           int(input("Digite o último número: ")))

print(f"Você digitou os seguintes números: {numeros}")
# Printo a lista: "NUMEROS"

if 5 in numeros:
    # Caso o nº 5 apareça em Lista: "NUMEROS"
    print(f"O número 5 apareceu {numeros.count(5)} vez(ez)")
    # Conto a quantidade de vezes que apareceu
    print(f"O nº 5 apareceu pela 1ª vez na {numeros.index(5)} posição")
    # Determino a 1º Posição em que "5" apareceu

print(f"Os nº pares da sequência são: ", end="")
# Escrevo For apenas para Printar os Pares
for numb in numeros:
    if numb % 2 == 0:
        print(f"{numb}", end=" ")




