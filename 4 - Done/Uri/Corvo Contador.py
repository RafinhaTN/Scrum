grito = 0  # Valor que simboliza o fim do processo
dec = 0

while grito < 3:

    action = str(input())  # Recebe uma ação: Decodifica o Olha ou quebra no grito: Caw Caw

    if action != "caw caw":
        codigo = ""  # Recebe o número em binário

        for olho in range(3):  # Traduzo o código do olho para binário
            if action[olho] == "-":
                codigo += "0"

            elif action[olho] == "*":
                codigo += "1"

        for i in range(3):  # Transcrevo o binário em decimal
            dec += int(codigo[-1 - i]) * (2 ** i)

    if action == "caw caw":  # Quebro o a sequência de soma do olho
        print(dec)
        grito += 1
        dec = 0
