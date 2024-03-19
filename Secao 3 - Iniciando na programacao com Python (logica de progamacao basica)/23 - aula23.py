# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')

if not senha:
    print('Você não digitou a senha')

print(not True) # False
print(not False) # True