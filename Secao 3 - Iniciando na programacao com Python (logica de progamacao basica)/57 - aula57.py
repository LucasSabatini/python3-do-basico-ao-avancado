"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com erros
de índices inexistentes na lista
"""
import os

lista_compras = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        lista_compras.append(input('Item: '))

    if opcao == 'a':
        try:
            if not lista_compras:
                print('Nada para apagar')

            if lista_compras:
                apagar_item = input('Escolha o índice para apagar: ')
                apagar_item_int = int(apagar_item)
                item_encontrado = False
                for indice, item in enumerate(lista_compras):
                    if indice == apagar_item_int:
                        item_encontrado = True
                        lista_compras.pop(indice)
                        print('Item apagado!')
                        
                if not item_encontrado:
                    print('Índice não encontrado!')
        except:
            print('Digite um índice válido!')

    if opcao == 'l':
        os.system('clear')
        if not lista_compras:
            print('Nada para listar')

        for indice, item in enumerate(lista_compras):
            print(indice, item)
        