import random
import PySimpleGUI as sg
from time import sleep

class Dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Deseja gerar um novo valor? (sim/nao) '
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Criar ação
        try:
            if self.eventos == 'sim':
                self.gerarValor()
            elif self.eventos == 'não':
                print('Até a próximaaaa...')
            else:
                print('Ação inválida')
        except:
            print('Erro ao processar seus dados!')

    def gerarValor(self):
        print('Jogando dado',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.')
        sleep(0.5)
        print(f'Valor: {random.randint(self.valor_minimo, self.valor_maximo)}')

novo_dado = Dado()
novo_dado.iniciar()