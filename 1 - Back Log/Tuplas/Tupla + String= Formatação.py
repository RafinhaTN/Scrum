materiais_escolares = ("Borracha", 2.00, "Caneta", 1.50, "Caderno", 14.00,
                       "Estojo", 20.50, "Lápis", 2.00, "Régua", 4.00)

print("-=-" * 15)
print(f"{'LISTA DE PREÇOS, LOJINHA DO TIÃO':^40}")
#  Printo "Lista de Preços" com 40 espaços e com o Texto centralizado = "^"
print("-=-" * 15)
for pos in range(len(materiais_escolares)):
    if pos % 2 == 0:
        print(f"{materiais_escolares[pos]:.<30}", end="")
        # Printo o material e preencho de pontos até dar 30 posições
    else:
        print(f"R${materiais_escolares[pos]:>7.2f}")
        # Printo o valor e dou um "ESPAÇO" de 7 posições de "R$"
