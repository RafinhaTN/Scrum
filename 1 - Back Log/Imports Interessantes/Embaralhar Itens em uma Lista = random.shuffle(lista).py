import random

lista_numeros = [input("Digite um valor: "), input("Digite um valor: "),
                 input("Digite um valor: "), input("Digite um valor: ")]

random.shuffle(lista_numeros)
# Randomiza a Lista de Números
print(f"O valor escolhido foi: {lista_numeros}")