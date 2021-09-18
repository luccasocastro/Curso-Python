class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando o banco de dados...')
            print('Cadastrar o usuário {}, idade {}'.format(nome, idade))
        else:
            print('Dados inválidos')


