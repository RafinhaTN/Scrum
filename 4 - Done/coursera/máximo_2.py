def maximo(a, b):
    if a > b:
        return a
    if b > a:
        return b


x, y = input().split()
x, y = int(x), int(y)
z = maximo(x, y)
print(z)
