nome_completo = input("Digite seu nome completo: ").strip()
# Remover todos os Espaços Desnecessários

nome = nome_completo.split()
# Separa os NOMES do Nome Inteiro

print(f"O seu nome em Maiúsculo é: {nome_completo.upper()}")
# Transforma todas as Letras de Nome_Completo em Maiúscula
print(f"O seu nome em minúsculo é: {nome_completo.lower()}")
# Transforma todas as Letras de Nome_Completo em Minúscula
print(f"O seu nome tem {len(nome_completo) - nome_completo.count(' ')} letras")
# Conta a Quantidade de Letras no Nome_Completo tirando os Espaços
print(f"O seu 1º nome é: {nome[0]} e ele tem {len(nome[0])}")
# Determina o seu Primeiro Nome
