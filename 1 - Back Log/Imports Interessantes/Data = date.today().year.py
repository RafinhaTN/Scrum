from datetime import date

ano = int(input("Que ano você deseja analisar???"
                " Caso deseje ver o ano atual, digite 0... : "))

if ano == 0:
    # Caso o INPUT seja 0, ele analisa a data de hoje
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # Se a DATA tiver as condições anteriores para ser BISSEXTO
    print(f"O ano de {ano} é BISSEXTO")
else:
    print(f"O ano de {ano} NÃO é BISSEXTO")
