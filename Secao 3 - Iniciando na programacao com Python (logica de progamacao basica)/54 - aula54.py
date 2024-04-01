"""
Exercício
Exiba os índices da lista
0 Lucas
1 Elisa
2 Marco
"""
lista = ['Lucas', 'Elisa', 'Marco']
lista.append('Edson')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista)[indice])