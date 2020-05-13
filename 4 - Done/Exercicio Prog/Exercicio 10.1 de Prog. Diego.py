from time import sleep

quant_numb = int(input("Digite quantos nº você deseja colocar na sua sequência: "))
sequencia = []  # Criei uma sequencia(lista)

for i in range(quant_numb):  # Adicionava o nº na sequência
    sequencia.append(input("Digite o {} nº da sequência: ".format(i + 1)))

print("A sequência é: {}".format(sequencia))
print("A sequência invertida é: {}".format(sequencia[quant_numb:: -1]))

sleep(3)
print("-=-" * 30)
print("BOM... Não sei se você quer eles fora da lista, então me dá um minutinho ...")
print("-=-" * 30)
sleep(3)

invertida = sequencia[quant_numb:: -1]
print("A sequência invertida fora da Lista ----> ", end="")

for valores in invertida:
    print(valores, end="  ")