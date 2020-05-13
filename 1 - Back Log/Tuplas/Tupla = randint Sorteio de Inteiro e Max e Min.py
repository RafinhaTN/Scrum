from random import randint

numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f"Os valores sorteados foram {numeros}")
print(f"O menor valor da sequência foi {min(numeros)}")
print(f"O maior valor da sequência foi {max(numeros)}")