
while True:
    texto = str(input())
    new_texto = ""

    for i in range(len(texto)):

        if texto[i] == "p" and texto[i - 1] == "p" or texto[i] == "s" and texto[i - 1] == "s":
            print("", end="")


        elif texto[i] == "s" or texto[i] == "x" or texto[i] == "v" or texto[i] == "j" or texto[i] == "b" or texto[i] == "p":
            print("f", end="")


        elif texto[i] == "S" or texto[i] == "X" or texto[i] == "V" or texto[i] == "J" or texto[i] == "B" or texto[i] == "P":
            print("F", end="")

        else:
            print(texto[i], end="")

    print(new_texto)

