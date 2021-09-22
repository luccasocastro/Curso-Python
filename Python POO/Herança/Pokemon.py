class Pokemon:
    def __init__(self, nome, nvl):
        self.nome = nome
        self.nvl = nvl

    def ataque_basico(self):
        if self.nvl < 10:
            print('Arranhão')
        elif self.nvl < 20:
            print('Cabeçada')
        elif self.nvl < 30:
            print('Slash')


class Eletrico(Pokemon):
    def __init__(self, nome, nvl):
        super(Eletrico, self).__init__(nome, nvl)

    def ataque_basico(self):
        print('Thundershock')

class Grama(Pokemon):
    def __init__(self, nome, nvl):
        super(Grama, self).__init__(nome, nvl)

    def ataque_basico(self):
        print('Vine Whip')

class Aquatico(Pokemon):
    def __init__(self, nome, nvl):
        super(Aquatico, self).__init__(nome, nvl)

    def ataque_basico(self):
        print('Bubble')

class Lutar:
    def __init__(self, pkm1: Pokemon, pkm2: Eletrico):
        self.pkm1 = pkm1
        self.pkm2 = pkm2

    def batalha(self):
        if self.pkm1.nvl > self.pkm2.nvl:
            print(f'{self.pkm1.nome} tem vantagem')
        else:
            print(f'{self.pkm2.nome} tem vantagem')


rattata = Pokemon('Rattata', 15)
pikachu = Eletrico('Pikachu', 25)
bulbasaur = Grama('Bulbasaur', 13)
squirtle = Aquatico('Squirtle', 9)
battle = Lutar(rattata, pikachu)

rattata.ataque_basico()
pikachu.ataque_basico()
bulbasaur.ataque_basico()
squirtle.ataque_basico()
battle.batalha()
