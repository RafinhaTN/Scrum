nome = input("Digite um nome de uma cidade: ").strip().upper()
# Remover espaços desnecessários, além de tranformar o "x" em Maiúsculo

cidade = nome.split()
# Corto o nome em Tuplas e identifico se tem tal termo no Nome

print(cidade[0] == "SANTO")
# Apresenta o valor Booleano se o Primeiro Nome da Cidade é igual a "SANTO"
