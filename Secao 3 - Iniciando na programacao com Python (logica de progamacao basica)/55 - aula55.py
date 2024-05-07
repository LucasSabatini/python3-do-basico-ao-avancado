"""
Introdução ao desempacotamento + tuples (tuplas)
Tipo tupla - Uma lista imutável
"""
nomes = ['Lucas', 'Elisa', 'Marco']
#   nomes = tuple(nomes)
#   nomes = list(nomes)
# nomes[1] = 'outro'
_, nome, *_ = nomes
print(nomes)
print(nome)
