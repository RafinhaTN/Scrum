def primo(p):
    i = 0

    while i < p:
        i += 1
        if (p // i != 1 and p % i == 0 and i != 1) or p == 1:  # Estabeleço as relações de NÃO existencia de um Primo
            return False

    else:  # Caso seja primo, retorna TRUE
        return True


n = int(input("Digite quantos casos testes você irá executar: "))
resp = 0

for cont in range(n):  # Contagem de 1 até N
    num = int(input("Digite um número: "))

    if primo(num):  # Se o valor == TRUE, somo ele na variavel "resp"
        resp += num

print(resp)
