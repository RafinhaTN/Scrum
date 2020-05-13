def menor_e_maior(a, b, c):
    while a > b or b > c:
        if a > b:
            a, b = b, a

        if b > c:
            b, c = c, b

    return a, c


x, y, z = input().split()
x, y, z = int(x), int(y), int(z)
menor, maior = menor_e_maior(x, y, z)
print(menor, maior)