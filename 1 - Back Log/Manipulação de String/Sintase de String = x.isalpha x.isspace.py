alguma_coisa = input("Digite algo: ")

print(f"O tipo primitivo desse objeto é {type(alguma_coisa)}")
# Determino o Tipo de "alguma_coisa"
print(f"Só tem espaços??? {alguma_coisa.isspace()}")
# Verifico se "alguma_coisa" é apenas Espaços
print(f"Só é numero??? {alguma_coisa.isnumeric()}")
# Verifico se "alguma_coisa" é apenas Número
print(f"Só é alfabeto?? {alguma_coisa.isalpha()}")
# Verifico se "alguma_coisa" é apenas Letras
print(f"É maiúsculo??? {alguma_coisa.isupper()}")
# Verifico se "alguma_coisa" é Maiúsculo
print(f"É alphanumerico??? {alguma_coisa.isalnum()}")
# Verifico se "alguma_coisa" é AlphaNumérico = Número + Alfabeto
