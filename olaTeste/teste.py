class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
class pessoa_fisica(Pessoa):
    def __init__(self, nome: str, cpf: str) -> None:
        super().__init__(nome)
        self.cpf = cpf

    def status(self) -> None:
        print('=-'*3)
        print('STATUS')
        print('=-'*3)
        print(f'Pessoa Física:\nNome: {self.nome}\nCPF: {self.cpf}')

class pessoa_juridica(Pessoa):
    def __init__(self, nome: str, empresa: str) -> None:
        super().__init__(nome)
        self.empresa = empresa
    
    def status(self) -> None:
        print('=-'*3)
        print('STATUS')
        print('=-'*3)
        print(f'Pessoa Jurídica:\nNome: {self.nome}\nCPF: {self.empresa}')


