frase = input("Digite uma Frase/Texto: ").upper().strip()
# Remover todos os Espaços Desnecessários e transforma os termos em letra Maiúscula

print(f"A letra A apareceu {frase.count('A')} vezes")
# Conta quantas letras "A" tem na FRASE
print(f"A letra A apareceu na Primeira vez na Posição {frase.find('A') + 1}")
# Encontra a 1º Letra "A" da Esquerda para Direita
print(f"A letra A apareceu em Última vez na Posição {frase.rfind('A') + 1}")
# Encontra a 1º Letra "A" da Direita para Esquerda
