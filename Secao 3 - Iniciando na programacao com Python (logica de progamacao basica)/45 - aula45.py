"""
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto:
texto = iter('Lucas') # __iter__()
print(next(texto)) # __next__()


outro_texto = 'Sabatini'
iterador = iter(outro_texto) # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in outro_texto:
    print(letra)
