brasil = []
estado = {}

for tentativas in range(0, 2):
    estado["Unidade Federativa: "] = str(input("Digite o nome do Estado: "))
    estado["Sigla: "] = str(input("Digite a sigla do Estado: "))
    brasil.append(estado.copy())
    # Caso eu não usa-se o COPY, a lista BRASIL iria ser o último ESTADO 2x

for dicionario in brasil:  # Para cada dicionário em Brasil
    for unidade_federativa, sigla in dicionario.items():
        # Os termos UNIDADE_FEDERATIVA e SIGLA ficam respectivamento com o KEY_TERMO e VALUE do "dicionario"
        print(f"No Estado {unidade_federativa} a sigla é: {sigla}")
