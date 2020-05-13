numero = int(input())

for i in range(numero - 1, 0, -1):
    numero *= i

if numero == 0:
    numero = 1

print(numero)
