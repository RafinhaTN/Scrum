def bonitinho(frase):
    print("-=-" * 30)
    print(frase)
    print("-=-" * 30)


times = ("Corinthians", "Vasco", "Palmeiras",
         "Flamengo", "Curitiba", "São Paulo",
         "Santos", "Grêmio", "Operário",
         "Fluminense")
# Tupla de Times de Futebol

bonitinho(f"O time que está em 1º e 2º colocado são: {times[0:2]}")
# Printo os 2 Primeiros Termos

bonitinho(f"O time que está em penúltimo e em ultimo colocado são {times[-2:]}")
# Printo os 2 Últimos Termos

bonitinho(f"O times em Ordem Alfabética são: {sorted(times)}")
# Coloco a Tupla em Ordem Alfabética

bonitinho(f"O time do Palmeiras está na {times.index('Palmeiras') + 1}ª Colocação")
# Encontro o Palmeiras dentro da Tupla
