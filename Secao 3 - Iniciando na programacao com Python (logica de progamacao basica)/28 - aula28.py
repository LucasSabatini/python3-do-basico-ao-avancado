"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
letras = len(nome)

if nome and idade:
    primeira_letra = nome[0]
    ultima_letra = nome[-1]

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    
    print(f'Seu nome tem {letras} letras')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A última letra do seu nome é {ultima_letra}')
else:
    print('Desculpe, você deixou campos vazios.')
