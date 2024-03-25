frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
j = 0
freq_maior = 0
letra_maior_freq = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    freq_letra = frase.count(letra_atual)

    if freq_maior < freq_letra:
        freq_maior = freq_letra
        letra_maior_freq = letra_atual

    i += 1


print('A letra que apareceu mais vezes foi '
      f'{letra_maior_freq}. '
      f'Apareceu: {freq_maior} vezes')
