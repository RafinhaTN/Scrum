print("Está na tomada?")
prim_pergunta = str(input()).upper()

if prim_pergunta == "NÃO":
    print("Ligue na tomada")

elif prim_pergunta == "SIM":
    print("O monitor está ligando?")
    seg_pergunta = str(input()).upper()

    if seg_pergunta == "SIM":
        print("Arrume o computador")
    elif seg_pergunta == "NÃO":
        print("Arrume o monitor")