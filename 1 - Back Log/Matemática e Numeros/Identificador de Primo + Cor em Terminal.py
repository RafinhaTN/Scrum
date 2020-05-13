numb = int(input("Digite um número: "))
div = 0

for i in range(1, numb + 1):
    if numb % i == 0:
        # Caso o VALOR seja divisível por algum termo(i) e o resto seja = 0
        print(f"\033[33m", end="")
        # O \033[33m simboliza que você pintará o termo(i) por AMARELO
    else:
        print(f"\033[31m", end="")
        # O \033[33m simboliza que você pintará o termo(i) por VERMELHO
        div += 1

    print(f"{i}\033[m", end=" ")
    # O \033[m reseta a cor do termo(i) para BRANCO

if div <= 2:
    print("\nO nº inserido NÃO é um nº PRIMO")
    # Se o nº tiver mais que 2 DIVISORES(O próprio "NUMB" e "1"), ele não será primo
else:
    print("\nO nº inserido é um nº PRIMO")
