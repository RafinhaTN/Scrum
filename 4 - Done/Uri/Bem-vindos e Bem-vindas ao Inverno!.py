temp_a, temp_b, temp_c = input().split()
temp_a, temp_b, temp_c = int(temp_a), int(temp_b), int(temp_c)

prim_mudanca = temp_b - temp_a
seg_mudanca = temp_c - temp_b

if prim_mudanca < 0 and seg_mudanca >= 0:
    print(":)")

elif prim_mudanca > 0 and seg_mudanca <= 0:
    print(":(")

elif prim_mudanca > 0 and seg_mudanca > 0:
    if prim_mudanca > seg_mudanca:
        print(":(")
    else:
        print(":)")

elif prim_mudanca < 0 and seg_mudanca < 0:
    if prim_mudanca < seg_mudanca:
        print(":)")
    else:
        print(":(")

elif prim_mudanca == 0:
    if seg_mudanca > 0:
        print(":)")
    else:
        print(":(")

