popul_a, popul_b, crescimento_a, crescimento_b = input().split()
popul_a, popul_b = int(popul_a), int(popul_b)
cresc_a, cresc_b = float(crescimento_a)/100, float(crescimento_b)/100
anos = 0

while popul_a < popul_b:
    popul_a = int(popul_a * (1 + cresc_a))
    popul_b = int(popul_b * (1 + cresc_b))
    anos += 1

print(anos)