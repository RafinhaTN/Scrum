dados = [[input("Digite seu nome: "), int(input("Digite sua idade: "))]]
maior = 0
menor = dados[0][1]

while input("Deseja continuar [S/N]: ").upper() != "N":
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    dados.append([nome, idade])

for cont, i in enumerate(dados):
    if i[1] > maior:
        maior = i[1]

for cont, i in enumerate(dados):
    if i[1] < menor:
        menor = i[1]

print(f"O número de pessoas cadastradas foram: {len(dados)}")
print(f"A maior idade das pessoas cadastradas foi de {maior} anos")
print(f"A menor idade das pessoas cadastradas foi de {menor} anos")
