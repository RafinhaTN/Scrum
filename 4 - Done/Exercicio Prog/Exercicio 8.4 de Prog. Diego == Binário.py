valor = int(input("Digite um valor: "))
resp_bin = ""

while valor != 0:
    resto = valor % 2 # Pegar o resto da divisão por 2
    resp_bin += str(resto) # Salvar o valor obtido em uma variável
    valor = valor // 2 # Troco valor pelo o quociente da divisão por 2

binario = resp_bin[::-1] # Para resultado invertido

print("O valor digitado, em binário é ---> {}".format(binario))
