class ControleRemoto:

    def __init__(self):
        self.__volume = 50
        self.__ligado = False
        self.__tocando = False

    def getVolume(self):
        return self.__volume

    def setVolume(self, volume):
        self.__volume = volume

    def getLigado(self):
        return self.__ligado

    def setLigado(self, ligado):
        self.__ligado = ligado

    def getTocando(self):
        return self.__tocando

    def setTocando(self, tocando):
        self.__tocando = tocando

    def ligar(self):
        self.setLigado(True)

    def desligar(self):
        self.setLigado(False)
        self.setVolume(0)

    def abrirMenu(self):
        print(f'Está ligado? {self.getLigado()}')
        print(f'Está tocando? {self.getTocando()}')
        print(f'Volume: {self.getVolume()}')

    def fecharMenu(self):
        print('Fechando menu...')

    def maisVolume(self):
        if self.getLigado():
            self.setVolume(self.getVolume() + 5)
        else:
            print('Impossível aumentar volume')

    def menosVolume(self):
        if self.getLigado():
            self.setVolume(self.getVolume() - 5)
        else:
            print('Impossível diminuir volume')

    def ligarMudo(self):
        if self.getLigado() and self.getVolume() > 0:
            self.setVolume(0)

    def desligarMudo(self):
        if self.getLigado() and self.getVolume() == 0:
            self.setVolume(50)

    def play(self):
        if self.getLigado() and not self.getTocando():
            self.setTocando(True)

    def pause(self):
        if self.getLigado() and self.getTocando():
            self.setTocando(False)

