from psycopg2 import connect
from crud import *
from os import system
from time import sleep

connect, cursor = conectar_db()

while True:
    system('cls')
    print('=-'*10)
    print('\tMENU')
    print('=-'*10)
    print('1 - Cadastrar novo usuário')
    print('2 - Remover usuário')
    print('3 - Listar todos os usuários')
    print('4 - Buscar apenas um usuário')
    print('5 - Atualizar cadastros')
    print('6 - Sair')
    op = int(input('Informe a opção desejada: '))

    if op == 1:
        criar_usuario(connect, cursor)
        sleep(1)
    elif op == 2:
        remover_usuario(connect, cursor)
        sleep(1)
    elif op == 3:
        selecionar_todos(connect, cursor)
        system('pause')
    elif op == 4:
        selecionar_um(connect, cursor)
        system('pause')
    elif op == 5:
        atualizar_registro(connect, cursor)
        sleep(1)
    elif op == 6:
        desconectar_db(connect, cursor)
        sleep(1)
        system('cls')
        print('Goodbye!!!')
        sleep(1)
        system('cls')
        break
