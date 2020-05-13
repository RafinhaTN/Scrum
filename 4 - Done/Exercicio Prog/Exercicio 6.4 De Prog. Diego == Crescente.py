def crescente_3(a, b, c):
    while True: #só usei while pois quero praticar
        if a > b:
            a, b = b, a
        elif b > c:
            b, c = c, b
        else:
            break
    return a, b, c


x, y, z = input().split()
x, y, z = int(x), int(y), int(z)
answer = crescente_3(x, y, z)
print(answer)
