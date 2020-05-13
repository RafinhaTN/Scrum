nome = input("Digite seu nome completo: ").strip().upper()
# Remover espaços desnecessários, além de tranformar o "x" em Maiúsculo

nome = nome.split()
# Corto o nome em Tuplas e identifico se tem tal termo no Nome

print(f"O nome inserido tem Silva (???) ---> {'SILVA' in nome}")
# Apresenta o valor Booleano se SILVE in NOME
