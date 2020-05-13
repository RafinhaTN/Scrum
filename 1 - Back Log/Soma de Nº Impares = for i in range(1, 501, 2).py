impar = 0
contador = 0

for i in range(1, 501, 2):  # Apenas de Nº impares, logo pula de 2 em 2
    if i % 3 == 0:
        impar += i
        contador += 1

print(f"A soma resulta em {impar} e ele somou {contador} valores")
