"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_str)
    
    if numero_int % 2 == 0:
        print(f'Seu número {numero_int} é par!')

    elif numero_int % 2 != 0:
        print(f'Seu número {numero_int} é ímpar!')

except:
    print('Você não digitou um número inteiro!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia se 0-11, Boa tarde se 12-17 e Boa noite se 18-23.
"""
hora_digitada = input('Digite apenas a hora atual: ')

try:
    hora_int = int(hora_digitada)
    
    if hora_int >= 0 and hora_int <=11:
        print('Bom dia!')

    elif hora_int >= 12 and hora_int <=17:
        print('Boa tarde!')

    elif hora_int >= 18 and hora_int <=23:
        print('Boa noite!')

    else:
        print('Essa hora não existe!')

except:
    print('Você não digitou uma hora inteira!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6, escreva "Seu nome é muito grande."
"""
primeiro_nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(primeiro_nome)

if tamanho_nome > 1:
    if tamanho_nome >= 0 and tamanho_nome <= 4:
        print('Seu nome é curto!')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal!')
    elif tamanho_nome >= 7:
        print('Seu nome é muito grande!')
else:
    print('Digite mais de uma letra')
