#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_price(product):
    '''
        function to return the product value from its string
    '''
    product = product.split('(')
    product = product[1].split(',')

    return int(product[0])


def add_product(action, products, total):
    '''
        function to add product in cart
    '''
    if action == 5:
        product = 'Arroz (20,00)'
    elif action == 6:
        product = 'Feijão (10,00)'
    elif action == 7:
        product = 'Biscoito (5,00)'
    elif action == 8:
        product = 'Farinha (2,00)'
    elif action == 9:
        product = 'Macarrão (3,00)'

    total += get_price(product)
    products.append(product)
    print(f'\n  {product} foi adicionado no seu carrinho!')
    return [products, total]


def remove_product(products, total):
    '''
        function to remove product in cart
    '''

    print(f'''\n
    -----------------------------------
            CARRINHO DE COMPRAS
    -----------------------------------
    ''')

    counter = 0

    for product in products:
        print(f'    {counter} - {product}')
        counter += 1

    product = int(input('''
    ------------------------------
    Informe o número do produto que deseja remover:

    '''))

    if not 0 <= product < len(products):
        print('\n   Produto não encontrado!')
    else:
        total -= get_price(products[product])
        products.pop(product)
        print(f'\n  O produto {product} foi removido')

    return [products, total]

def get_products(products, total):
    '''
        function to return the products in the cart
    '''

    print(f'''\n
    -----------------------------------
            CARRINHO DE COMPRAS        
    -----------------------------------
    ''')

    counter = 1

    for product in products:
        print(f'    {counter} - {product}')
        counter += 1

    print(f'''
    ---------------------------------
    TOTAL: R$ {total},00
    ---------------------------------
    ''')


def menu():
    '''
        function to show the home menu
    '''

    print('''\n
    --------------------------------
                OPÇÕES
    --------------------------------
    0 - Finalizar Compra
    1 - Ver produtos no carrinho
    2 - Remover produto do carrinho
    --------------------------------
            PRODUTOS
    ------------------------------
    5 - Arroz (20,00)
    6 - Feijão (10,00)
    7 - Biscoito (5,00)
    8 - Farinha (2,00)
    9 - Macarrão (3,00)
    ------------------------------
        ''')

    action = int(input('    Digite uma das opções acima: '))

    return action


def main():
    '''
        function main
    '''

    products = []
    total = 0

    while True:
        action = menu()

        if action == 0:
            get_products(products, total)
            break
        elif action == 1:
            get_products(products, total)
            input(' Aperte enter para continuar')
        elif action == 2:
            response = remove_product(products, total)
            products = response[0]
            total = response[1]
        elif 5 <= action <= 9:
            response = add_product(action, products, total)
            products = response[0]
            total = response[1]

    print(' OBRIGADO POR USAR O NOSSO SISTEMA')


main()
