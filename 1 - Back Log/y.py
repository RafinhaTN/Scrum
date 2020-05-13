x = int(input())
bin = ""
i = 0
while x > 0:
    resto = x % 2
    x = x // 2
    bin += str(resto)

if x % 2 == 0 and not x == 0:
    new_bin = ""
    num = int(bin)
    for i in range(len(bin)):
        ult = num % 10
        new_bin += str(ult)
        num = (num - ult) // 10

    bin = new_bin

print(bin)
