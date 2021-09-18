class Pessoa: #substantivo
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome #substantivo
        self.idade = idade #substantivo

    def dirigir(self, veiculo: str) -> None: #verbos
        print(f'Dirigindo um(a) {veiculo}')

    def cantar(self) -> None: #verbos
        print('lalalala')

    def apresentar_idade(self) -> int: #verbos
        return self.idade

