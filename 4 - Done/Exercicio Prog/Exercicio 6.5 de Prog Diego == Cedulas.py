def cedulas(val):
    m20 = val // 20
    resto = val % 20
    m10 = resto // 10
    resto = resto % 10
    m5 = resto // 5
    resto = resto % 5
    m1 = resto // 1

    print(m20, "cédulas de $20")
    print(m10, "cédulas de $10")
    print(m5, "cédulas de $5")
    print(m1, "cédulas de $1")


dinheiro = int(input())
cedulas(dinheiro)
