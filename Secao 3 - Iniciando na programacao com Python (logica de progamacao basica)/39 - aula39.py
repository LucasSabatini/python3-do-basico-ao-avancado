"""
Iterando strings com while
"""

#       012345678910111213
nome = 'Lucas Sabatini' # Iteráveis

indice = 0
while indice < len(nome):
    if nome[indice] == ' ':
        print('* ', end='')
    else:
        print('*' + nome[indice], end='')

    indice += 1

print()

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)