x = int(input())
number = str(x)

if number[0] == number[-1]:
    print(" O número :{}, tem o primeiro e o último dígito iguais." .format(x))
else:
    print(" O número :{}, não tem o primeiro e o último dígito iguais.".format(x))
