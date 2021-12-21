import psycopg2
from time import sleep

def connect_db():
    host = 'localhost'
    dbname = 'company'
    user = 'postgres'
    password = 'lukita10'

    connect_string = 'host={0} user={1} dbname={2} password={3}'.format(host, user, dbname, password)
    connect = psycopg2.connect(connect_string)

    cursor = connect.cursor()

    cursor.execute("DROP TABLE IF EXISTS inventory;")

    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")

    return connect, cursor

def disconnect_db(connect, cursor):
    cursor.close()
    connect.close()
    print('Desconexão efetuada!!!')
    sleep(1)

def include_product(connect, cursor):
    nome = input('Informe o nome do produto: ')
    qntd = input('Informe a qntd que deseja adicionar: ')

    cursor.execute('INSERT INTO inventory (name, quantity) VALUES (%s, %s);', (nome, qntd))

    connect.commit()
    print('Produto adicionado com sucesso!!!')
    sleep(1)

def remove_product(connect, cursor):
    nome = input('Informe o nome produto que deseja remover: ')

    cursor.execute('DELETE FROM inventory WHERE name = %s;', (nome,))

    connect.commit()
    print('Produto removido com sucesso!!!')
    sleep(1)

def display_all_products(connect, cursor):
    cursor.execute('SELECT * FROM inventory;')

    rows = cursor.fetchall()

    for row in rows:
        print("-> (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
    sleep(3)
    
    connect.commit()

def update_stock(connect, cursor):
    nome = input('Informe o nome do produto que deseja modificar: ')
    qntd = input('Informe a quantidade que deve ser atualizada: ')

    cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;",(qntd,nome))
    print('Quantidade atualizada com sucesso!!!')
    sleep(1)

    connect.commit()




