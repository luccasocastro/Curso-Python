import random
from tkinter import *

class DiceRoller(object):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=('arial', 100))
        button = Button(master, text='Rolar Dados', command = self.roll)
        button.place(x=200, y=0)
    
    def roll(self):
        valorMinimo = 1
        valorMaximo = 20
        # symbols = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.label.config(text=f'[{random.randint(valorMinimo, valorMaximo)}] [{random.randint(valorMinimo, valorMaximo)}]')
        self.label.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Jogo de Dados')
    root.geometry('500x200')
    DiceRoller(root)
    root.mainloop()
    