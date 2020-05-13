def vogal(x):
    if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False


letra = str(input()).upper()
resp = vogal(letra)
print(resp)
