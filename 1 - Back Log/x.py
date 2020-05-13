ficha = []

for i in range(0, 4):
    print(f"---------- FICHA {i + 1} -----------")
    nome = str(input("Qual o seu nome: "))
    idade = str(input("Digite sua idade: "))
    sexo = str(input("Informe seu sexo[M/F]: "))

    inf = [nome, idade, sexo]
    ficha.append(inf)

print(f"{ficha[0][1]}")
print(f"Média das Idades == {[sum(linha[i][1]) for i in ficha]}")
