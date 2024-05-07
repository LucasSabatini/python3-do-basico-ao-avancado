"""
enumaerate - enumera iteráveis (índices)
"""
lista = ['Lucas', 'Elisa', 'Marco']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for tupla_enumerada in enumerate(lista):
#     print("FOR da Tupla:")
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
