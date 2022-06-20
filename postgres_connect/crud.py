import psycopg2
from getpass import getpass

# construindo a string de conexão e a tabela
def conectar_db():
    # criando os componentes da string de conexão
    host = 'localhost'
    user = 'postgres'
    dbname = 'usuario'
    password = 'lukita10'

    conn_string = 'host={0} user={1} dbname={2} password={3}'.format(host,user,dbname,password)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print('Conexão efetuada com sucesso!!')

    return conn, cursor

def criando_tabela(cursor):
    cursor.execute('DROP TABLE IF EXISTS usuario;')
    cursor.execute('CREATE TABLE usuario (id CHAR(5) CONSTRAINT pk_id PRIMARY KEY, nome VARCHAR(40), email VARCHAR(40), senha VARCHAR(40));')

# realizando a disconexão com o banco de dados
def disconectar_db(conn, cursor):
    cursor.close()
    conn.close()
    print('Disconectado!')

# CREATE
def criar_usuario(conn, cursor):
    nome = input('Informe o nome do usuário: ')
    email = input('Informe o email: ')
    senha = getpass('Informe a senha: ')
    # comando para executar um comando sql
    cursor.execute('INSERT INTO usuario (nome, email, senha) VALUES (%s,%s,%s);', (nome,email,senha))
    conn.commit()

# READ
# selecionar todos os dados:
def selecionar_todos(conn, cursor):
    cursor.execute('SELECT * FROM usuario;')
    rows = cursor.fetchall()

    for row in rows:
        print("-> (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
    
    conn.commit()

# selecionar apenas um dado:
def selecionar_um(conn, cursor):
    id = int(input('Informe um id válido: '))

    cursor.execute('SELECT * FROM usuario WHERE id=%s;', (id,))

    row = cursor.fetchall()
    print('-> (%s, %s, %s)' %(str(row[0]), str(row[1]), str(row[2])))

    conn.commit()

# UPDATE
def atualizar_registro(conn, cursor):
    id = int(input('Informe o id do usuario que deseja atualizar: '))
    nome = input('Informe o novo nome: ')
    email = input('Informe o novo email: ')
    senha = getpass('Informe a nova senha: ')
    cursor.execute('UPDATE usuario SET nome=%s, email=%s, senha=%s WHERE id=%s;',(nome,email,senha,id))

    conn.commit()

# DELETE
def remover_usuario(conn, cursor):
    id = int(input('Informe o id do usuário que deseja remover: '))

    cursor.execute('DELETE FROM usuario WHERE id=%s;',(id,))

    print('Usuário removido!!')

    conn.commit()




