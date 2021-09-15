from datetime import datetime

class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self,assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        elif self.falando:
            print(f'{self.nome} já está falando.')
            return
        else:
            print(f'{self.nome} está falando sobre {assunto}')
            self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} já está calado.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        elif self.falando:
            print(f'{self.nome} não pode comer pois está falando.')
            return
        else:
            print(f'{self.nome} está comendo!')
            self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

