def par_impar(a):
    """
    ------> Funçao que serve para "printar" o n!(=x + y)
    :param a: simboliza se a lista será dos termos pares ou impares
    :return: retorna nada
    """
    i = 0
    while i < len(a):
        if i < len(a) - 1:
            print("{} +".format(a[i]), end=" ")
        else:
            print("{})".format(a[i]))
        i += 1
    return

lim = int(input()) #limite de splits
numbers = input().split()
i = somapar = somaimpar = 0
par = []
impar = []

while i < lim:

    if int(numbers[i]) % 2 == 0:
        par.append(numbers[i])
        somapar += int(numbers[i])

    elif int(numbers[i]) % 2 != 0:
        impar.append(numbers[i])
        somaimpar += int(numbers[i])
    i += 1
i = 0


print("{}(=".format(somapar), end="") #"printar" o n!
par_impar(par)

print("{}(=".format(somaimpar), end="") #"printar" o n!
par_impar(impar)



