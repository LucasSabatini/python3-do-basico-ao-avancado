nome = 'Lucas Sabatini'
altura = 1.71
peso = 65
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} metros de altura'
linha_2 = f'pesa {peso:.2f} quilos'
linha_3 = f'e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# print(nome, 'tem',
    #   altura, 'metros de altura,', 'pesa', peso, 'quilos',
    #   'e seu IMC é', imc)