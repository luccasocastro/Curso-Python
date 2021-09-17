class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print(f'{self.nome} está correndo!')

    def __apresentar_documento(self):
        return self.__cpf

    def beber(self, bebida):
        if bebida == 'cerveja':
            print(f'cpf: {self.__apresentar_documento()}')
            if self.idade >= 18:
                print(f'{self.nome} está bebendo {bebida}')
            else:
                print(f'{self.nome} não pode beber {bebida}')
        else:
            print(f'{self.nome} está bebendo {bebida}')







