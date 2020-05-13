lista = []

for num in range(0, 6):
    lista.append(int(input(f"Determino o valor da posição {num}: ")))
    # Adiciono valores na LISTA

print(f"Você digitou a seguinte lista: {lista}")  # Imprime a LISTA
print(f"O menor valor dessa lista é: {min(lista)}. Localizado na posição: ", end="")
# Determino o MENOR valor da LISTA
for pos, i in enumerate(lista):
    # Se o valor(i) for igual ao MENOR da Lista, printo a posição
    if i == min(lista):
        print(f"{pos}", end=" ")
print()

print(f"O maior valor dessa lista é: {max(lista)}. Localizado na posição: ", end="")
# Determino o MAIOR valor da LISTA
for pos, i in enumerate(lista):
    # Se o valor(i) for igual ao MAIOR da Lista, printo a posição
    if i == max(lista):
        print(f"{pos}", end=" ")
print()