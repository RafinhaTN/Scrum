def maior_primo(primo):
    list_primo = []

    for num_primo in range(primo + 1):
        cont = 1

        while cont < num_primo:
            if (num_primo // cont != 1 and num_primo % cont == 0 and cont != 1) or num_primo == 1:
                break
            cont += 1

        else:
            list_primo.append(num_primo)

    return list_primo[-1]


x = int(input())
resp = maior_primo(x)
print(resp)
