lista = [input("Digite um valor: "), input("Digite um valor: "),
         input("Digite um valor: "), input("Digite um valor: "),
         input("Digite um valor: "), input("Digite um valor: ")]

lista = [int(x) for x in lista]

for cont, i in enumerate(lista):
    print(f"Na posição {cont} se encontra o valor: {i}")