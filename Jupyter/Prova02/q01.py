from psycopg2 import connect
from time import sleep
from moduloq01 import *
from os import system

connect, cursor = connect_db()

while True:
    system('cls')
    print('=-'*10)
    print('\tMENU')
    print('=-'*10)
    print('1 - Incluir novo produto')
    print('2 - Remover produto')
    print('3 - Listar todos os produtos')
    print('4 - Atualizar estoque')
    print('5 - Sair')
    op = int(input('Informe a opção desejada: '))

    if op == 1:
        include_product(connect, cursor)
    elif op == 2:
        remove_product(connect, cursor)
    elif op == 3:
        display_all_products(connect, cursor)
    elif op == 4:
        update_stock(connect, cursor)
    elif op == 5:
        disconnect_db(connect, cursor)
        print('Goodbye!!!')
        break
