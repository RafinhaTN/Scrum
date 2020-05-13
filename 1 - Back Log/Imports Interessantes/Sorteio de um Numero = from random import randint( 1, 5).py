from random import randint
from time import sleep


def arrumadinho():
    print("-=-" * 20)
    print("Vou pensar em um número de 1 até 5. Tente advinhar....")
    print("-=-" * 20)


arrumadinho()

computador = randint(1, 5)  # Randomiza um Nº entre 1 e 5
numero = int(input("Que nº eu pensei ??? : "))  # Escolha

print("PROCESSANDO......")
sleep(2)

if computador == numero:
    print("PARABÉNS!!! Você advinhou!!!")

else:
    print(f"Infelizmente tu ERROU, o nº que eu escolhi foi {computador}")
